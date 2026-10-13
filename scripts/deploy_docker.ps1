param(
    [Parameter(Mandatory = $true)][string]$Image,
    [Parameter(Mandatory = $true)][string]$ContainerName,
    [Parameter(Mandatory = $true)][string]$VolumeName,
    [Parameter(Mandatory = $true)][int]$HostPort,
    [Parameter(Mandatory = $true)][string]$BuildId
)

$ErrorActionPreference = "Stop"
$projectLabelKey = "com.news-publishing.project"
$projectLabelValue = "news-publishing-devops"
$candidateName = "$ContainerName-candidate-$BuildId"
$backupName = "$ContainerName-previous-$BuildId"
$candidateCreated = $false
$previousRenamed = $false
$newContainerCreated = $false
$previousWasRunning = $false
$previousContainer = $null

function Invoke-Docker {
    param(
        [Parameter(Mandatory = $true)][string[]]$Arguments,
        [switch]$AllowFailure
    )

    $savedPreference = $ErrorActionPreference
    try {
        $ErrorActionPreference = "Continue"
        $output = & docker @Arguments 2>&1
        $exitCode = $LASTEXITCODE
    }
    finally {
        $ErrorActionPreference = $savedPreference
    }
    $text = ($output | ForEach-Object { "$_" }) -join [Environment]::NewLine
    if ($exitCode -ne 0 -and -not $AllowFailure) {
        throw "docker $($Arguments -join ' ') failed with exit code $exitCode. $text"
    }

    return [pscustomobject]@{
        ExitCode = $exitCode
        Output = $text
    }
}

function Get-Container {
    param([Parameter(Mandatory = $true)][string]$Name)

    $listed = Invoke-Docker -Arguments @("ps", "--all", "--filter", "name=^$Name$", "--format", "{{.Names}}")
    if ($listed.Output.Trim() -ne $Name) {
        return $null
    }

    $result = Invoke-Docker -Arguments @("inspect", $Name)
    $containers = ConvertFrom-Json -InputObject $result.Output
    return $containers[0]
}

function Assert-ProjectContainer {
    param(
        [Parameter(Mandatory = $true)]$Container,
        [Parameter(Mandatory = $true)][string]$Name
    )

    $label = $Container.Config.Labels.$projectLabelKey
    $imageMatchesProject = $Container.Config.Image -match '^news-publishing-app:'
    if ($label -ne $projectLabelValue -and -not $imageMatchesProject) {
        throw "Container '$Name' is not identified as this project's deployment. It will not be changed."
    }
}

function Wait-ForHealthy {
    param(
        [Parameter(Mandatory = $true)][string]$Name,
        [int]$TimeoutSeconds = 90
    )

    $deadline = (Get-Date).AddSeconds($TimeoutSeconds)
    while ((Get-Date) -lt $deadline) {
        $container = Get-Container -Name $Name
        if ($null -eq $container) {
            throw "Container '$Name' disappeared while waiting for health."
        }
        if ($container.State.Status -ne "running") {
            throw "Container '$Name' stopped in state '$($container.State.Status)'."
        }
        if ($container.State.Health -and $container.State.Health.Status -eq "healthy") {
            return
        }
        if ($container.State.Health -and $container.State.Health.Status -eq "unhealthy") {
            throw "Container '$Name' reported unhealthy."
        }
        Start-Sleep -Seconds 3
    }

    throw "Container '$Name' did not become healthy within $TimeoutSeconds seconds."
}

function Test-ExternalHealth {
    param([Parameter(Mandatory = $true)][string]$Url)

    for ($attempt = 1; $attempt -le 20; $attempt++) {
        try {
            $response = Invoke-WebRequest -Uri $Url -UseBasicParsing -TimeoutSec 5
            $body = $response.Content | ConvertFrom-Json
            if (
                $response.StatusCode -eq 200 -and
                $body.status -eq "ok" -and
                $body.message -eq "News Publishing Workflow MVP running"
            ) {
                Write-Host "External health check passed on attempt ${attempt}: $Url"
                return
            }
        }
        catch {
            Write-Host "Waiting for application health (attempt $attempt/20): $($_.Exception.Message)"
        }
        Start-Sleep -Seconds 3
    }

    throw "The deployed endpoint did not return the expected healthy response: $Url"
}

function Write-ContainerLogs {
    param([string]$Name)

    $container = Get-Container -Name $Name
    if ($null -ne $container) {
        try {
            Assert-ProjectContainer -Container $container -Name $Name
            Write-Host "Logs for ${Name}:"
            $result = Invoke-Docker -Arguments @("logs", $Name) -AllowFailure
            Write-Host $result.Output
        }
        catch {
            Write-Host "Skipped logs for '$Name' because project ownership could not be verified."
        }
    }
}

try {
    Invoke-Docker -Arguments @("info") | Out-Null

    $existingNames = Invoke-Docker -Arguments @("ps", "--filter", "publish=$HostPort", "--format", "{{.Names}}")
    $publishedNames = @($existingNames.Output -split "\r?\n" | Where-Object { $_ })
    foreach ($name in $publishedNames) {
        if ($name -ne $ContainerName) {
            throw "Host port $HostPort is published by unrelated container '$name'. No container was changed."
        }
    }

    $previousContainer = Get-Container -Name $ContainerName
    if ($null -ne $previousContainer) {
        Assert-ProjectContainer -Container $previousContainer -Name $ContainerName
        $previousWasRunning = $previousContainer.State.Running
    }

    $portListeners = @(Get-NetTCPConnection -LocalPort $HostPort -State Listen -ErrorAction SilentlyContinue)
    if ($portListeners.Count -gt 0 -and $publishedNames -notcontains $ContainerName) {
        throw "Host port $HostPort has a listener not verified as the project's Docker container. Identify it and stop it through its owner; Jenkins will not terminate host processes."
    }

    if ($null -ne (Get-Container -Name $candidateName)) {
        throw "Candidate container '$candidateName' already exists. Inspect it manually; Jenkins will not remove it."
    }
    if ($null -ne (Get-Container -Name $backupName)) {
        throw "Backup container '$backupName' already exists. Inspect it manually; Jenkins will not replace it."
    }

    $volume = Invoke-Docker -Arguments @("volume", "ls", "--filter", "name=^$VolumeName$", "--format", "{{.Name}}")
    if ($volume.Output.Trim() -ne $VolumeName) {
        Invoke-Docker -Arguments @("volume", "create", "--label", "$projectLabelKey=$projectLabelValue", $VolumeName) | Out-Null
    }

    Write-Host "Starting isolated health-check candidate from $Image."
    Invoke-Docker -Arguments @(
        "run", "--detach", "--name", $candidateName,
        "--label", "$projectLabelKey=$projectLabelValue",
        $Image
    ) | Out-Null
    $candidateCreated = $true
    Wait-ForHealthy -Name $candidateName
    Invoke-Docker -Arguments @("rm", "--force", $candidateName) | Out-Null
    $candidateCreated = $false

    if ($null -ne $previousContainer) {
        if ($previousWasRunning) {
            Write-Host "Stopping the verified existing project container before reusing port $HostPort."
            Invoke-Docker -Arguments @("stop", "--time", "20", $ContainerName) | Out-Null
        }
        Invoke-Docker -Arguments @("rename", $ContainerName, $backupName) | Out-Null
        $previousRenamed = $true
    }

    Write-Host "Starting $ContainerName on host port $HostPort with persistent volume $VolumeName."
    Invoke-Docker -Arguments @(
        "run", "--detach", "--name", $ContainerName,
        "--label", "$projectLabelKey=$projectLabelValue",
        "--publish", "${HostPort}:5001",
        "--volume", "${VolumeName}:/data",
        "--env", "DATABASE_PATH=/data/app.db",
        $Image
    ) | Out-Null
    $newContainerCreated = $true

    Wait-ForHealthy -Name $ContainerName
    Test-ExternalHealth -Url "http://127.0.0.1:$HostPort/health"

    if ($previousRenamed) {
        $backup = Get-Container -Name $backupName
        Assert-ProjectContainer -Container $backup -Name $backupName
        Invoke-Docker -Arguments @("rm", $backupName) | Out-Null
        $previousRenamed = $false
    }

    Write-Host "Deployment succeeded: image=$Image container=$ContainerName port=${HostPort}:5001 volume=$VolumeName"
}
catch {
    $deploymentError = $_.Exception.Message
    Write-Host "Docker deployment failed: $deploymentError"
    Write-ContainerLogs -Name $candidateName
    Write-ContainerLogs -Name $ContainerName
    Write-ContainerLogs -Name $backupName

    $rollbackError = $null
    try {
        $current = Get-Container -Name $ContainerName
        $currentIsFailedBuild = (
            $null -ne $current -and
            $current.Config.Image -eq $Image -and
            $current.Config.Labels.$projectLabelKey -eq $projectLabelValue
        )
        if (
            $null -ne $current -and
            ($newContainerCreated -or ($previousRenamed -and $currentIsFailedBuild))
        ) {
            Assert-ProjectContainer -Container $current -Name $ContainerName
            if ($current.State.Running) {
                Invoke-Docker -Arguments @("stop", "--time", "20", $ContainerName) | Out-Null
            }
            Invoke-Docker -Arguments @("rm", $ContainerName) | Out-Null
        }

        if ($previousRenamed) {
            $backup = Get-Container -Name $backupName
            if ($null -ne $backup) {
                Assert-ProjectContainer -Container $backup -Name $backupName
                Invoke-Docker -Arguments @("rename", $backupName, $ContainerName) | Out-Null
                if ($previousWasRunning) {
                    Invoke-Docker -Arguments @("start", $ContainerName) | Out-Null
                }
            }
        }
    }
    catch {
        $rollbackError = $_.Exception.Message
    }

    if ($null -ne $rollbackError) {
        throw "$deploymentError Rollback also failed: $rollbackError"
    }
    throw $deploymentError
}
finally {
    if ($candidateCreated) {
        $candidate = Get-Container -Name $candidateName
        if ($null -ne $candidate) {
            Assert-ProjectContainer -Container $candidate -Name $candidateName
            Invoke-Docker -Arguments @("rm", "--force", $candidateName) | Out-Null
        }
    }
}

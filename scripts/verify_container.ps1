param(
    [Parameter(Mandatory = $true)][string]$ContainerName
)

$ErrorActionPreference = "Stop"
$inspection = & docker inspect $ContainerName 2>&1
if ($LASTEXITCODE -ne 0) {
    throw "Could not inspect container '$ContainerName': $inspection"
}

$container = (ConvertFrom-Json -InputObject ($inspection -join [Environment]::NewLine))[0]
if ($container.State.Status -ne "running") {
    throw "Container '$ContainerName' is not running (state: $($container.State.Status))."
}
if ($null -eq $container.State.Health -or $container.State.Health.Status -ne "healthy") {
    $health = if ($container.State.Health) { $container.State.Health.Status } else { "not configured" }
    throw "Container '$ContainerName' is not healthy (health: $health)."
}
if (-not $container.NetworkSettings.Ports.'5001/tcp') {
    throw "Container '$ContainerName' has no published mapping for container port 5001."
}

Write-Host "Container $ContainerName is running and healthy."
Write-Host "Published port: $($container.NetworkSettings.Ports.'5001/tcp'[0].HostPort):5001"

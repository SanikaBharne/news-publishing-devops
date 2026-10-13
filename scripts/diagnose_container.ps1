param(
    [Parameter(Mandatory = $true)][string]$ContainerName
)

$ErrorActionPreference = "Stop"
$inspection = & docker inspect $ContainerName 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "No inspectable container named '$ContainerName' is available for diagnostics."
    exit 0
}

$container = (ConvertFrom-Json -InputObject ($inspection -join [Environment]::NewLine))[0]
$label = $container.Config.Labels.'com.news-publishing.project'
$imageMatchesProject = $container.Config.Image -match '^news-publishing-app:'
if ($label -ne "news-publishing-devops" -and -not $imageMatchesProject) {
    Write-Host "Skipped logs: ownership of '$ContainerName' could not be verified."
    exit 0
}

Write-Host "Container state: $($container.State.Status)"
if ($container.State.Health) {
    Write-Host "Container health: $($container.State.Health.Status)"
}
& docker logs $ContainerName
if ($LASTEXITCODE -ne 0) {
    throw "Could not read logs for verified project container '$ContainerName'."
}

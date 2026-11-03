$ErrorActionPreference = "Continue"
$engineType = & docker info --format "{{.OSType}}" 2>&1
$exitCode = $LASTEXITCODE

if ($exitCode -ne 0) {
    throw "Docker Engine is unavailable to this Jenkins account: $engineType"
}
if (($engineType | Out-String).Trim() -ne "linux") {
    throw "This pipeline requires Docker Desktop's Linux container engine; detected '$engineType'."
}

Write-Host "Docker Engine is available and configured for Linux containers."

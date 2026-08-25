$ErrorActionPreference = "Stop"

# ================================================
$ZipUrl = "https://github.com/TheRake66/python-fast/raw/refs/heads/main/release.zip"
$AppFolder = "Fast"
$DestDir = Join-Path $env:APPDATA $AppFolder
$TempZip = Join-Path $env:TEMP ("install_" + (Get-Random) + "_" + (Get-Random) + ".zip")

# ================================================
try {
    Write-Host "Download in progress..." -ForegroundColor Cyan
    Invoke-WebRequest -Uri $ZipUrl -OutFile $TempZip
} catch {
    Write-Host "Download failed. Check your internet connection!" -ForegroundColor Red
    exit 1
}

# ================================================
try {
    Write-Host "Decompression..." -ForegroundColor Cyan
    if (-not (Test-Path $DestDir)) {
        New-Item -ItemType Directory -Path $DestDir | Out-Null
    }
    Expand-Archive -Path $TempZip -DestinationPath $DestDir -Force
} catch {
    Write-Host "Decompression failed!" -ForegroundColor Red
    if (Test-Path $DestDir) { Remove-Item $DestDir -Recurse -Force }
    if (Test-Path $TempZip) { Remove-Item $TempZip -Force }
    exit 1
}

# ================================================
try {
    Write-Host "Installation with pip..." -ForegroundColor Cyan
    Set-Location $DestDir
    pip install -e .
} catch {
    Write-Host "Unable to install the command using pip!" -ForegroundColor Red
    if (Test-Path $DestDir) { Remove-Item $DestDir -Recurse -Force }
    if (Test-Path $TempZip) { Remove-Item $TempZip -Force }
    exit 1
}

# ================================================
Write-Host "Installation done." -ForegroundColor Green
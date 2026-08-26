$ErrorActionPreference = "Stop"

$ZipUrl = "https://github.com/TheRake66/python-fast/raw/refs/heads/main/release.zip"
$DestDir = Join-Path $env:APPDATA "Fast"
$TempZip = Join-Path $env:TEMP "install_$PID.zip"
$Venv =  "$DestDir\.venv"
$VenvScripts = "$Venv\.Scripts"

try {
    $ErrorMsg = "Unable to download file archive!"
    Write-Host "Download in progress..." -ForegroundColor Cyan
    Invoke-WebRequest -Uri $ZipUrl -OutFile $TempZip

    $ErrorMsg = "Unable to decompress file archive!"
    Write-Host "Decompression..." -ForegroundColor Cyan
    New-Item -ItemType Directory -Path $DestDir -Force | Out-Null
    Expand-Archive -Path $TempZip -DestinationPath $DestDir -Force

    $ErrorMsg = "Unable to install the command using pip!"
    Write-Host "Installation with pip..." -ForegroundColor Cyan
    python -m venv "$Venv"
    & "$VenvScripts\pip.exe" install -e "$DestDir" -q --disable-pip-version-check

    $ErrorMsg = "Unable to updating path variable!"
    Write-Host "Updating path variable..." -ForegroundColor Cyan
    $UserPath = [Environment]::GetEnvironmentVariable("Path", "User")
    if ($UserPath -notlike "*$VenvScripts*") {
        [Environment]::SetEnvironmentVariable("Path", "$UserPath;$VenvScripts", "User")
        $env:Path += ";$VenvScripts"
    }

    $ErrorMsg = "Unable to clean the installation!"
    Write-Host "Cleaning installation..." -ForegroundColor Cyan
    Remove-Item $TempZip -Force

    Write-Host "Installation done." -ForegroundColor Green
} catch {
    Write-Host $ErrorMsg -ForegroundColor Red
    exit 1
}
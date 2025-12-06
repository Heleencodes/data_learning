Write-Host ""
Write-Host "==============================================="
Write-Host "   Entity Extraction Environment Setup"
Write-Host "==============================================="
Write-Host ""

function Install-PackageIfMissing {
    param ([string]$package)

    Write-Host "Checking: $package..."

    $exists = pip show $package 2>$null

    if ($exists) {
        Write-Host "Package already installed: $package"
    } else {
        Write-Host "Installing: $package ..."
        pip install $package
        Write-Host "Installed: $package"
    }
}

Install-PackageIfMissing -package "spacy"
Install-PackageIfMissing -package "pandas"

Write-Host ""
Write-Host "Checking spaCy model..."

$cmd = "import importlib; print('INSTALLED' if importlib.util.find_spec('en_core_web_sm') else 'MISSING')"
$spacyModel = python -c $cmd

Write-Host "Model check result: $spacyModel"

if ($spacyModel -eq "INSTALLED") {
    Write-Host "spaCy model already available."
} else {
    Write-Host "Downloading spaCy model..."
    python -m spacy download en_core_web_sm
    Write-Host "spaCy model installed."
}

Write-Host ""
Write-Host "Checking directories..."

$dirs = @("input","output","scripts","database","docs")

foreach ($d in $dirs) {
    if (!(Test-Path $d)) {
        New-Item -ItemType Directory -Path $d | Out-Null
        Write-Host "Created directory: $d"
    } else {
        Write-Host "Directory exists: $d"
    }
}

Write-Host ""
Write-Host "==============================================="
Write-Host " Setup complete!"
Write-Host "==============================================="

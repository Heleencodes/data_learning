$PublicPath = "C:\Users\Openbaar"

Write-Host "Opschonen gestart voor: $PublicPath" -ForegroundColor Cyan

# Mappen die we willen bewaren
$ProtectedFolders = @(
    "Openbare documenten\Native Instruments",
    "Openbare documenten\Noise Engineering",
    "Openbare documenten\Softube"
)

# Bestanden die veilig verwijderd mogen worden
$DeleteFiles = @(
    "main.py",
    "README.md"
)

# Mappen die veilig verwijderd mogen worden
$DeleteFolders = @(
    ".github",
    ".vscode",
    "Openbare afbeeldingen",
    "Openbare muziek",
    "Openbare video's",
    "Openbare downloads",
    "Openbaar bureaublad",
    "Openbare accountafbeeldingen"
)

# Verwijder losse bestanden
foreach ($file in $DeleteFiles) {
    $filePath = Join-Path $PublicPath $file
    if (Test-Path $filePath) {
        Remove-Item $filePath -Force
        Write-Host "✔ Verwijderd: $file"
    }
}

# Verwijder rommel-mappen
foreach ($folder in $DeleteFolders) {
    $folderPath = Join-Path $PublicPath $folder
    if (Test-Path $folderPath) {
        Remove-Item $folderPath -Recurse -Force
        Write-Host "✔ Map verwijderd: $folder"
    }
}

# Lege mappen verwijderen, behalve de beschermde
$allFolders = Get-ChildItem $PublicPath -Directory -Recurse
foreach ($folder in $allFolders) {

    $relative = $folder.Ful

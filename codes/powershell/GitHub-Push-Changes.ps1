$Path = 'C:\Users\DxZCr\Documents\GitHub\'

$Folders = Get-ChildItem -Path $Path

$Date = Get-Date


foreach ($Item in $Folders.Name)
{
    if ($Item -eq ".vscode")
    {
        continue
    }
    else
    {
        Write-Host "******* Working on $Item Repository *******" -ForegroundColor Green
        Set-Location -Path "$Path\$Item"
        git pull -q
        git add -A 
        git commit -m "$Date" -q
        git push -q
    }   
}

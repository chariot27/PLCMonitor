# Script Inteligente para rodar a API MBSR
$pythonCmd = "python"

if (Get-Command "py" -ErrorAction SilentlyContinue) {
    $pythonCmd = "py"
} elseif (Get-Command "python3" -ErrorAction SilentlyContinue) {
    $pythonCmd = "python3"
} elseif (Get-Command "python" -ErrorAction SilentlyContinue) {
    $pythonCmd = "python"
} else {
    Write-Error "Python não encontrado! Por favor, instale o Python ou verifique se ele está no PATH."
    exit
}

Write-Host "Iniciando API com: $pythonCmd" -ForegroundColor Cyan
& $pythonCmd -m uvicorn main:app --reload --port 8000 --host 0.0.0.0

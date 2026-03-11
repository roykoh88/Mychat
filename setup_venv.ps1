# conda 환경 Mychat에 의존성 설치 + 베이스 모델 다운로드
# 프로젝트 폴더(mychat)에서 실행: .\setup_venv.ps1

$condaEnv = "Mychat"
$projectRoot = $PSScriptRoot
$downloadScript = Join-Path $projectRoot "scripts\download_models.py"

# 1. pip 업그레이드
Write-Host "[1/3] pip 업그레이드 (conda: $condaEnv)" -ForegroundColor Cyan
conda run -n $condaEnv python -m pip install --upgrade pip --progress-bar on

# 2. 의존성 설치
Write-Host "[2/3] 패키지 설치 (requirements.txt)" -ForegroundColor Cyan
conda run -n $condaEnv pip install -r requirements.txt --progress-bar on
if ($LASTEXITCODE -ne 0) {
    Write-Host "설치 실패 시: CUDA/PyTorch 환경에 따라 Unsloth 공식 가이드를 따르세요." -ForegroundColor Yellow
    Write-Host "  https://github.com/unslothai/unsloth" -ForegroundColor Gray
    exit 1
}

# 3. 베이스 모델 다운로드
Write-Host "[3/3] 베이스 모델 다운로드 (Hugging Face 캐시)" -ForegroundColor Cyan
$env:PYTHONUNBUFFERED = "1"
if (Test-Path $downloadScript) {
    conda run -n $condaEnv python -u $downloadScript
} else {
    $tempScript = Join-Path $projectRoot "_download_models_temp.py"
    @"
from huggingface_hub import snapshot_download
for name in ['unsloth/meta-llama-3.1-8b-unsloth-bnb-4bit', 'unsloth/llama-3.2-1b-bnb-4bit']:
    print('[다운로드]', name)
    snapshot_download(repo_id=name)
    print('[완료]', name)
print('전체 다운로드 완료.')
"@ | Set-Content -Path $tempScript -Encoding UTF8
    try {
        conda run -n $condaEnv python -u $tempScript
    } finally {
        if (Test-Path $tempScript) { Remove-Item $tempScript -Force }
    }
}
if ($LASTEXITCODE -ne 0) {
    Write-Host "모델 다운로드 실패. 앱 첫 실행 시 자동 다운로드 시도됨." -ForegroundColor Yellow
} else {
    Write-Host "모델 다운로드 완료." -ForegroundColor Green
}

# 4. 설치 확인
Write-Host "`n[설치 확인]" -ForegroundColor Cyan
$packages = @("fastapi", "uvicorn", "jinja2", "unsloth")
foreach ($pkg in $packages) {
    $ver = conda run -n $condaEnv pip show $pkg 2>$null | Select-String "Version:"
    if ($ver) {
        Write-Host "  $pkg : " -NoNewline
        Write-Host ($ver -replace "Version: ", "").Trim() -ForegroundColor Green
    } else {
        Write-Host "  $pkg : " -NoNewline
        Write-Host "설치 안 됨" -ForegroundColor Yellow
    }
}
$checkScript = Join-Path $projectRoot "scripts\check_models.py"
if (Test-Path $checkScript) {
    Write-Host "`n  모델(어댑터) 경로:" -ForegroundColor Gray
    conda run -n $condaEnv python $checkScript
}

Write-Host "`n완료. 아래처럼 활성화한 뒤 app.py를 실행하세요:" -ForegroundColor Green
Write-Host "  conda activate $condaEnv" -ForegroundColor White
Write-Host "  python app.py" -ForegroundColor White

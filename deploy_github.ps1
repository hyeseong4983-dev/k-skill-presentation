# GitHub CLI 배포 스크립트
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "   K-Skill 발표자료 GitHub 배포 마법사   " -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan

# 1. gh CLI 인증 상태 확인
$authCheck = gh auth status 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "`n[!] GitHub CLI 인증이 필요합니다. 웹 브라우저 인증을 시작합니다..." -ForegroundColor Yellow
    gh auth login --web -h github.com
}

# 2. GitHub 리포지토리 생성 및 원클릭 푸시
Write-Host "`n[*] GitHub 원격 저장소를 생성하고 발표자료를 푸시합니다..." -ForegroundColor Green
gh repo create k-skill-presentation --public --source=. --remote=origin --push

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n[V] 배포 성공! GitHub 리포지토리가 생성되었습니다." -ForegroundColor Green
    
    # 3. GitHub Pages 자동 활성화 시도
    Write-Host "[*] GitHub Pages 활성화 시도 중..." -ForegroundColor Cyan
    gh api -X POST "repos/{owner}/{repo}/pages" -f "source[branch]=master" -f "source[path]=/" 2>$null
    
    Write-Host "`n웹 브라우저에서 리포지토리를 엽니다..." -ForegroundColor Yellow
    gh repo view --web
} else {
    Write-Host "`n[X] 리포지토리 생성 또는 푸시 중 오류가 발생했습니다." -ForegroundColor Red
}

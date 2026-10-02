# 🇰🇷 K-Skill : AI 에이전트 한국어·한국 도메인 지능 생태계 발표자료

본 발표자료는 [NomaDamas/K-skill](https://github.com/NomaDamas/K-skill) 리포지토리의 크롤링 데이터 분석을 바탕으로 제작된 차세대 반응형 **HTML Slide Deck**입니다.

---

## 🌟 주요 특징 및 기술 스택

1. **인터랙티브 웹 애니메이션 (Anime.js)**
   - 슬라이드 전환 및 요소별 순차적 페이드인/바운스 애니메이션
   - 슬라이드 1 카운터 넘버 애니메이션 (`122+ 스킬`, `7.7k+ Stars`, `1,142+ Commits`, `96% 완결율`)
   - Manim 스타일의 배경 파티클 네트워크 캔버스 렌더링

2. **수식 및 알고리즘 벡터 렌더링 (Manim Style)**
   - 에이전트 의도 파싱부터 JSON 반환까지의 벡터 경로 SVG 동적 드로잉
   - 상태 전이 및 시간 복잡도($\mathcal{O}(1)$), 완결성 모델링

3. **고해상도 정량 데이터 분석 (Matplotlib)**
   - `assets/chart_categories.png`: 122개 이상 스킬의 5대 핵심 도메인 분포 도넛 차트
   - `assets/chart_benchmark.png`: 글로벌 기본 LLM vs K-Skill 탑재 에이전트 도메인 완결율 비교 바 차트

4. **Google Flow 아키텍처 다이어그램**
   - 구글 클라우드 / 머티리얼 스타일의 인터랙티브 플로우 파이프라인
   - 각 노드(Agent Core → K-Skill Router → Execution Cluster → Normalized JSON) 클릭 시 실시간 로그/입출력 시뮬레이션

5. **AI 생성 비주얼 에셋 (Nano Banana)**
   - `assets/hero_banner.jpg`: 서울 스카이라인 및 한국 전통 문양과 사이버네틱 신경망 결합 히어로 이미지
   - `assets/agent_flow.jpg`: 아이소메트릭 3D 에이전트 파이프라인 플로우 이미지

---

## 🕹️ 발표 슬라이드 조작법

- **다음 슬라이드**: `→` (오른쪽 화살표) / `Space` / `PageDown` / 화면 스와이프
- **이전 슬라이드**: `←` (왼쪽 화살표) / `PageUp`
- **전체화면 전환**: `F` 키
- **처음 / 끝**: `Home` / `End`
- **단축키 안내**: `?` 키

---

## 🚀 GitHub CLI 배포 방법

로컬 리포지토리가 이미 초기화되어 있습니다. 아래 명령어로 GitHub에 즉시 원클릭 배포할 수 있습니다:

```bash
# 1. GitHub CLI 로그인 (브라우저 인증)
gh auth login

# 2. 리포지토리 생성 및 원격 푸시
gh repo create k-skill-presentation --public --source=. --remote=origin --push
```

또는 제공된 자동화 스크립트를 실행하세요:
```powershell
.\deploy_github.ps1
```

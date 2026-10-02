import os
import matplotlib.pyplot as plt
import numpy as np

# Set dark theme style matching Google / modern tech deck
plt.style.use('dark_background')
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows Korean font
plt.rcParams['axes.unicode_minus'] = False

output_dir = os.path.join(os.path.dirname(__file__), 'assets')
os.makedirs(output_dir, exist_ok=True)

# 1. Chart: K-Skill Category Distribution (Donut Chart)
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(aspect="equal"), facecolor='#0f172a')
ax.set_facecolor('#0f172a')

categories = ['공공데이터/법률\n(경매·건축 등)', '포털/뉴스/트렌드\n(네이버·긱뉴스)', '금융/거시경제\n(한국은행·주식)', '부동산/도시정보\n(국토부·실거래가)', '개발/에이전트 유틸\n(CLI 어댑터)']
counts = [38, 32, 24, 18, 10]
colors = ['#4285F4', '#34A853', '#FBBC05', '#EA4335', '#A142F4']

wedges, texts, autotexts = ax.pie(
    counts,
    labels=categories,
    autopct='%1.1f%%',
    pctdistance=0.75,
    colors=colors,
    startangle=140,
    wedgeprops=dict(width=0.45, edgecolor='#1e293b', linewidth=2),
    textprops=dict(color='#cbd5e1', fontsize=11, weight='bold')
)

for autotext in autotexts:
    autotext.set_color('#ffffff')
    autotext.set_fontsize(12)
    autotext.set_weight('bold')

ax.set_title("K-Skill 122+ 스킬 생태계 도메인 분포", fontsize=15, color='#ffffff', weight='heavy', pad=20)
plt.tight_layout()
fig.savefig(os.path.join(output_dir, 'chart_categories.png'), dpi=300, facecolor='#0f172a')
plt.close(fig)

# 2. Chart: Agent Benchmark Comparison (Grouped Bar Chart)
fig, ax = plt.subplots(figsize=(9, 5), facecolor='#0f172a')
ax.set_facecolor('#0f172a')

domains = ['실시간 네이버 뉴스', '대법원 경매정보', '한국은행 ECOS 통계', '긱뉴스 최신 테크', '건축물대장 공공데이터']
standard_agent = [22, 5, 18, 12, 8]       # Global LLM without K-Skill
kskill_agent = [96, 92, 95, 98, 91]       # With K-Skill

x = np.arange(len(domains))
width = 0.35

rects1 = ax.bar(x - width/2, standard_agent, width, label='글로벌 기본 에이전트', color='#64748b', alpha=0.7)
rects2 = ax.bar(x + width/2, kskill_agent, width, label='K-Skill 탑재 에이전트', color='#38bdf8', edgecolor='#38bdf8', linewidth=1.5)

# Styling
ax.set_ylabel('한국 도메인 질의 완결 성공률 (%)', color='#cbd5e1', fontsize=12, labelpad=10)
ax.set_title('K-Skill 도입 전/후 한국 특화 태스크 완결율 비교', color='#ffffff', fontsize=14, weight='heavy', pad=15)
ax.set_xticks(x)
ax.set_xticklabels(domains, color='#e2e8f0', fontsize=11)
ax.tick_params(colors='#94a3b8')
ax.set_ylim(0, 115)
ax.grid(axis='y', color='#334155', linestyle='--', alpha=0.5)
ax.legend(facecolor='#1e293b', edgecolor='#475569', labelcolor='#ffffff', fontsize=11, loc='upper left')

# Value labels on bars
def autolabel(rects, is_highlight=False):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}%',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 4),  # 4 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=10,
                    weight='bold',
                    color='#38bdf8' if is_highlight else '#94a3b8')

autolabel(rects1)
autolabel(rects2, is_highlight=True)

for spine in ax.spines.values():
    spine.set_color('#334155')

plt.tight_layout()
fig.savefig(os.path.join(output_dir, 'chart_benchmark.png'), dpi=300, facecolor='#0f172a')
plt.close(fig)

print("Matplotlib charts successfully generated in assets folder.")

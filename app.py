import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# ---------------------------------------------------------
# 1. 페이지 테마 & 커스텀 CSS (모던 다크 대시보드 UI)
# ---------------------------------------------------------
st.set_page_config(
    page_title="VIBE Space Designer PRO",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    /* 메인 배경 및 폰트 설정 */
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    .main .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }
    
    /* 카드 스타일링 */
    div[data-testid="stMetric"] {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
    }
    
    /* Expander 모던화 */
    .streamlit-expanderHeader {
        background-color: #1e293b !important;
        border-radius: 8px !important;
        color: #38bdf8 !important;
    }
    
    /* 버튼 스타일 */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #2563eb;
        color: white;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. 세션 상태 초기화 (공간 레이아웃 & 대화 기록 & 시뮬레이션 상태)
# ---------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "안녕하세요! VIBE AI입니다. 원하시는 배치를 말씀하시거나 '시뮬레이션 시작'을 눌러 관람객 동선을 확인하세요."}
    ]

if "layout" not in st.session_state:
    st.session_state.layout = {
        "Main Stage": {"x": 8.0, "y": 5.0, "w": 2.5, "h": 6.0, "color": "#ef4444"},
        "Photo Zone": {"x": 3.0, "y": 7.0, "w": 3.0, "h": 3.0, "color": "#06b6d4"},
        "Food Zone": {"x": 3.0, "y": 2.5, "w": 3.5, "h": 2.5, "color": "#f59e0b"},
        "Entrance": {"x": 6.0, "y": 0.8, "w": 2.0, "h": 1.0, "color": "#3b82f6"}
    }

if "simulating" not in st.session_state:
    st.session_state.simulating = False

# ---------------------------------------------------------
# 3. 상단 헤더 & 접이식 채팅 기록
# ---------------------------------------------------------
st.title("⚡ VIBE SPACE DESIGNER (PRO)")

with st.expander("💬 대화 기록 보기 / 접기", expanded=False):
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

st.markdown("---")

# ---------------------------------------------------------
# 4. 메인 대시보드 레이아웃 (좌: 컨트롤/분석, 우: 시뮬레이션 캔버스)
# ---------------------------------------------------------
col_left, col_right = st.columns([1, 2.5])

with col_left:
    st.subheader("📊 Live Analysis & Control")
    
    # 시뮬레이션 제어 버튼
    if st.button("▶️ 동적 관람객 시뮬레이션 실행"):
        st.session_state.simulating = True

    st.write("")
    
    # 메트릭 카드가 들어갈 자리
    st.metric(label="평균 혼잡도 (Density)", value="68%", delta="-5% (최적화됨)")
    st.metric(label="최대 정체 구역", value="Main Stage")
    st.metric(label="유입 관람객 수", value="2,500 명")
    
    st.info("💡 **AI 실시간 제안**\nEntrance 주변 병목을 완화하기 위해 Photo Zone을 좌측 상단으로 조금 이동하는 것을 권장합니다.")

with col_right:
    st.subheader("🗺️ Interactive Venue Simulation Board")
    
    # Matplotlib 다크 모드 스타일 설정
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='#0f172a')
    ax.set_facecolor('#1e293b')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.grid(True, color='#334155', linestyle='--', alpha=0.5)

    # 1) 공간 구역(Zone) 렌더링
    for name, item in st.session_state.layout.items():
        rect = plt.Rectangle(
            (item["x"] - item["w"]/2, item["y"] - item["h"]/2),
            item["w"], item["h"],
            facecolor=item["color"], edgecolor='white', alpha=0.6, linewidth=1.5
        )
        ax.add_patch(rect)
        ax.text(item["x"], item["y"], name, ha='center', va='center', 
                fontweight='bold', color='white', fontsize=11)

    # 2) 관람객 입자(Particles) 시뮬레이션 로직
    num_particles = 120
    # 입구 좌표
    ent = st.session_state.layout["Entrance"]
    # 관람객 생성
    px = ent["x"] + np.random.uniform(-ent["w"]/3, ent["w"]/3, num_particles)
    py = ent["y"] + np.random.uniform(-ent["h"]/3, ent["h"]/3, num_particles)
    
    # 타겟(무대, 포토존, 푸드존) 중 랜덤 지정
    targets = [st.session_state.layout["Main Stage"], 
               st.session_state.layout["Photo Zone"], 
               st.session_state.layout["Food Zone"]]
    
    target_idx = np.random.choice(len(targets), size=num_particles, p=[0.5, 0.3, 0.2])
    tx = np.array([targets[i]["x"] for i in target_idx])
    ty = np.array([targets[i]["y"] for i in target_idx])

    # 시뮬레이션 상태일 때 가상 이동 처리
    if st.session_state.simulating:
        # 진행 정도에 따른 입자 위치 계산
        step = np.random.uniform(0.1, 0.8, num_particles)
        px = px + (tx - px) * step
        py = py + (ty - py) * step
        st.session_state.simulating = False # 1회 렌더링 후 리셋

    # 관람객(점) 점찍기
    ax.scatter(px, py, c='#f43f5e', s=25, alpha=0.8, edgecolors='white', linewidths=0.5, label='Attendees')
    
    # 밀도 Heatmap 표현
    x_grid, y_grid = np.meshgrid(np.linspace(0, 10, 80), np.linspace(0, 10, 80))
    z_density = np.zeros_like(x_grid)
    for x_p, y_p in zip(px, py):
        dist = np.sqrt((x_grid - x_p)**2 + (y_grid - y_p)**2)
        z_density += np.exp(-dist**2 / 0.8)
    
    ax.imshow(z_density, extent=[0, 10, 0, 10], origin='lower', cmap='YlOrRd', alpha=0.3)
    ax.legend(loc='upper left')

    # 차트 출력
    st.pyplot(fig)

# ---------------------------------------------------------
# 5. 하단 고정 채팅 입력창
# ---------------------------------------------------------
user_input = st.chat_input("요구사항을 입력하세요 (예: 무대 크기 축소해줘, 입구 더 크게 확장해줘)")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    response_text = "요청사항을 반영하여 대시보드 레이아웃을 수정했습니다."
    
    if "무대" in user_input and ("크게" in user_input or "확장" in user_input):
        st.session_state.layout["Main Stage"]["w"] = 3.5
        response_text = "Main Stage의 규격을 확장하여 관람 수용 인원을 늘렸습니다."
    elif "무대" in user_input and ("작게" in user_input or "축소" in user_input):
        st.session_state.layout["Main Stage"]["w"] = 2.0
        response_text = "Main Stage 크기를 축소하여 동선 공간을 넓혔습니다."
    elif "포토존" in user_input or "photo" in user_input.lower():
        st.session_state.layout["Photo Zone"]["x"] = 2.5
        st.session_state.layout["Photo Zone"]["y"] = 7.5
        response_text = "Photo Zone 위치를 좌측 상단으로 이동시켰습니다."
    elif "입구" in user_input:
        st.session_state.layout["Entrance"]["w"] = 3.0
        response_text = "Entrance 폭을 넓혀 병목 구간을 해소했습니다."

    st.session_state.messages.append({"role": "assistant", "content": response_text})
    st.rerun()

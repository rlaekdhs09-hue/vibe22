import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="VIBE Space Designer v4",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 커스텀 CSS (채팅 스타일 및 깔끔한 UI 디자인)
st.markdown("""
<style>
    .main .block-container {
        padding-top: 1.5rem;
        padding-bottom: 5rem;
    }
    .stChatMessage {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 8px;
    }
    .css-1544g2n {
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "안녕하세요! 행사장 공간 배치를 도와드리는 VIBE AI입니다. 원하시는 배치를 말씀해 주세요."}
    ]

if "layout" not in st.session_state:
    st.session_state.layout = {
        "Main Stage": {"x": 5, "y": 8, "w": 4, "h": 1.5, "color": "#FF6B6B"},
        "Photo Zone": {"x": 2, "y": 2, "w": 2, "h": 2, "color": "#4ECDC4"},
        "Food Zone": {"x": 8, "y": 2, "w": 2, "h": 2, "color": "#FFE66D"},
        "Entrance": {"x": 5, "y": 0.5, "w": 2, "h": 0.8, "color": "#1A535C"}
    }

# ---------------------------------------------------------
# 상단 헤더 및 접이식 대화 기록 (Expandable Chat History)
# ---------------------------------------------------------
st.title("🏛️ VIBE SPACE DESIGNER (v4)")

with st.expander("💬 이전 대화 기록 보기 / 접기", expanded=False):
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

st.markdown("---")

# ---------------------------------------------------------
# 메인 행사장 시뮬레이션 화면 (Heatmap & 공간 시뮬레이션)
# ---------------------------------------------------------
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("🗺️ Event Space Simulation")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_title("Venue Layout & Density Simulation", fontsize=14, fontweight='bold')

    # 혼잡도 Heatmap 레이어 생성
    x_grid, y_grid = np.meshgrid(np.linspace(0, 10, 100), np.linspace(0, 10, 100))
    z_density = np.zeros_like(x_grid)

    # 배치된 각 요소 그리기 및 혼잡도 생성
    for name, item in st.session_state.layout.items():
        rect = plt.Rectangle(
            (item["x"] - item["w"]/2, item["y"] - item["h"]/2),
            item["w"], item["h"],
            facecolor=item["color"], edgecolor='black', alpha=0.8, linewidth=1.5
        )
        ax.add_patch(rect)
        ax.text(item["x"], item["y"], name, ha='center', va='center', fontweight='bold', color='white' if item["color"] == "#1A535C" else 'black')
        
        # Heatmap 계산
        dist = np.sqrt((x_grid - item["x"])**2 + (y_grid - item["y"])**2)
        z_density += np.exp(-dist**2 / 2.0)

    # Heatmap 오버레이
    ax.imshow(z_density, extent=[0, 10, 0, 10], origin='lower', cmap='YlOrRd', alpha=0.3)

    st.pyplot(fig)

with col2:
    st.subheader("📊 공간 분석")
    st.metric(label="총 공간 이용률", value="68%", delta="안전")
    st.metric(label="예상 최대 혼잡구역", value="Main Stage")
    st.info("💡 입구 근처 동선 정체를 방지하기 위해 포토존 위치 조정을 권장합니다.")

# ---------------------------------------------------------
# 하단 고정 형태의 채팅 입력창 (Bottom Chat Input)
# ---------------------------------------------------------
user_input = st.chat_input("공간 배치 변경이나 요구사항을 입력하세요 (예: 무대를 더 크게 해줘)")

if user_input:
    # 사용자 메시지 저장
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # 간이 처리 로직 (입력에 맞춰 시뮬레이션 변형 예시)
    response = "요청사항을 반영하여 공간 배치를 업데이트했습니다."
    
    if "무대" in user_input and "크게" in user_input:
        st.session_state.layout["Main Stage"]["w"] = 6
        st.session_state.layout["Main Stage"]["h"] = 2
        response = "Main Stage의 크기를 더 크게 변경했습니다."
    elif "입구" in user_input:
        st.session_state.layout["Photo Zone"]["x"] = 2
        st.session_state.layout["Photo Zone"]["y"] = 1.5
        response = "포토존을 입구 근처로 이동시켰습니다."

    # AI 응답 저장
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 1. 페이지 설정
st.set_page_config(
    page_title="VIBE Space Designer v4",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 커스텀 CSS (여백 및 채팅 UI 다듬기)
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
</style>
""", unsafe_allow_html=True)

# 2. 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "안녕하세요! 행사장 인터랙티브 공간 설계를 도와드리는 VIBE AI입니다. 원하시는 배치를 말씀해 주세요."}
    ]

if "layout" not in st.session_state:
    st.session_state.layout = {
        "Main Stage": {"x": 5.0, "y": 8.0, "w": 4.0, "h": 1.5, "color": "#FF6B6B"},
        "Photo Zone": {"x": 2.0, "y": 2.0, "w": 2.0, "h": 2.0, "color": "#4ECDC4"},
        "Food Zone": {"x": 8.0, "y": 2.0, "w": 2.0, "h": 2.0, "color": "#FFE66D"},
        "Entrance": {"x": 5.0, "y": 0.5, "w": 2.0, "h": 0.8, "color": "#1A535C"}
    }

# 3. 상단 헤더 및 접이식 대화 기록
st.title("🏛️ VIBE SPACE DESIGNER (v4)")

with st.expander("💬 이전 대화 기록 보기 / 접기", expanded=False):
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

st.markdown("---")

# 4. 메인 공간 시뮬레이션 및 분석 화면
col_sim, col_info = st.columns([3, 1])

with col_sim:
    st.subheader("🗺️ Event Space Simulation Board")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.4)
    ax.set_title("Venue Layout & Density Simulation", fontsize=12, fontweight='bold')

    # 혼잡도 Heatmap 계산
    x_grid, y_grid = np.meshgrid(np.linspace(0, 10, 100), np.linspace(0, 10, 100))
    z_density = np.zeros_like(x_grid)

    # 공간 요소 그리기
    for name, item in st.session_state.layout.items():
        rect = plt.Rectangle(
            (item["x"] - item["w"]/2, item["y"] - item["h"]/2),
            item["w"], item["h"],
            facecolor=item["color"], edgecolor='black', alpha=0.85, linewidth=1.5
        )
        ax.add_patch(rect)
        
        # 라벨 표시
        text_color = 'white' if item["color"] == "#1A535C" else 'black'
        ax.text(item["x"], item["y"], name, ha='center', va='center', fontweight='bold', color=text_color, fontsize=10)
        
        # 밀도 계산
        dist = np.sqrt((x_grid - item["x"])**2 + (y_grid - item["y"])**2)
        z_density += np.exp(-dist**2 / 2.0)

    # Heatmap 오버레이
    ax.imshow(z_density, extent=[0, 10, 0, 10], origin='lower', cmap='YlOrRd', alpha=0.35)

    st.pyplot(fig)

with col_info:
    st.subheader("📊 공간 실시간 분석")
    st.metric(label="전체 공간 이용률", value="65%", delta="적정 범위")
    st.metric(label="최대 혼잡 예상 구역", value="Main Stage")
    st.info("💡 **동선 안내**\n입구 주변 병목 현상을 막기 위해 Photo Zone 위치 조정을 권장합니다.")

# 5. 하단 고정 채팅 입력창
user_input = st.chat_input("공간 변경 요구사항을 입력하세요 (예: 무대 크게 해줘, 포토존 이동해줘)")

if user_input:
    # 사용자 메시지 저장
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # 인터랙션 반영
    response_text = "요청사항을 반영하여 시뮬레이션 보드를 업데이트했습니다."
    
    if "무대" in user_input and ("크게" in user_input or "확장" in user_input):
        st.session_state.layout["Main Stage"]["w"] = 5.5
        st.session_state.layout["Main Stage"]["h"] = 2.0
        response_text = "Main Stage의 크기를 크게 확장했습니다."
        
    elif "포토존" in user_input or "photo" in user_input.lower():
        st.session_state.layout["Photo Zone"]["x"] = 3.0
        st.session_state.layout["Photo Zone"]["y"] = 3.0
        response_text = "Photo Zone 위치를 접근성이 좋은 측면으로 이동했습니다."
        
    elif "입구" in user_input:
        st.session_state.layout["Entrance"]["w"] = 3.0
        response_text = "입구 폭을 확장하여 동선을 확보했습니다."

    # 응답 저장 및 화면 리프레시
    st.session_state.messages.append({"role": "assistant", "content": response_text})
    st.rerun()

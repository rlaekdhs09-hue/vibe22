import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------
# 1. 페이지 설정 & 글로벌 테마 CSS
# ---------------------------------------------------------
st.set_page_config(
    page_title="VIBE Space Designer PRO",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    /* 다크 테마 배경 및 글로벌 폰트 */
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    
    /* 사이드바 스타일링 */
    section[data-testid="stSidebar"] {
        background-color: #1e293b !important;
        border-right: 1px solid #334155;
    }

    /* 카드 메트릭 디자인 */
    div[data-testid="stMetric"] {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
    }

    /* 히어로 세션 카드 디자인 */
    .hero-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 30px;
        margin-bottom: 20px;
    }

    /* 버튼 모던화 */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #2563eb;
        color: white;
        border: none;
        font-weight: bold;
        padding: 10px 16px;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. 세션 상태 초기화 (페이지 메뉴, 공간 배치, 대화 기록)
# ---------------------------------------------------------
if "current_page" not in st.session_state:
    st.session_state.current_page = "🏠 홈 화면"

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
# 3. 사이드바 메뉴 네비게이션
# ---------------------------------------------------------
with st.sidebar:
    st.title("⚡ VIBE SPACE")
    st.caption("AI 기반 행사장 설계 & 분석 플랫폼")
    st.markdown("---")
    
    page_selection = st.radio(
        "메뉴 선택",
        ["🏠 홈 화면", "📊 대시보드 & 시뮬레이션", "📑 AI 보고서 생성"],
        index=["🏠 홈 화면", "📊 대시보드 & 시뮬레이션", "📑 AI 보고서 생성"].index(st.session_state.current_page)
    )
    st.session_state.current_page = page_selection

# ---------------------------------------------------------
# PAGE 1: 🏠 홈 화면 (Landing Page)
# ---------------------------------------------------------
if st.session_state.current_page == "🏠 홈 화면":
    st.title("🚀 VIBE Space Designer에 오신 것을 환영합니다")
    st.caption("인공지능 기반 실시간 행사장 동선 시뮬레이션 및 안전 리포트 자동화 시스템")
    st.write("")

    # 히어로 섹션
    st.markdown("""
    <div class="hero-card">
        <h2>🏛️ 똑똑한 행사장 공간 설계의 시작</h2>
        <p style="color: #94a3b8; font-size: 16px;">
            AI 알고리즘이 관람객의 이동 패턴과 혼잡도를 분석하여 최적의 부스 배치 및 동선을 추천합니다.<br>
            대시보드에서 실시간 시뮬레이션을 실행하고, 한 클릭으로 종합 안전 보고서를 생성해 보세요.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 대시보드 만들기")
        st.write("대화형 AI 인터페이스로 무대, 포토존, 푸드존 위치를 자유롭게 조정하고 실시간 혼잡도 Heatmap을 확인하세요.")
        if st.button("👉 대시보드로 이동"):
            st.session_state.current_page = "📊 대시보드 & 시뮬레이션"
            st.rerun()

    with col2:
        st.subheader("📑 AI 보고서 만들기")
        st.write("현재 레이아웃의 안전성, 예상 관람객 밀도, 병목 위험 구역을 AI 분석으로 종합 정리한 PDF/텍스트 보고서를 자동 발급합니다.")
        if st.button("👉 AI 보고서 생성하기"):
            st.session_state.current_page = "📑 AI 보고서 생성"
            st.rerun()

# ---------------------------------------------------------
# PAGE 2: 📊 대시보드 & 시뮬레이션
# ---------------------------------------------------------
elif st.session_state.current_page == "📊 대시보드 & 시뮬레이션":
    st.title("📊 Space Design Dashboard")

    with st.expander("💬 AI 대화 기록 보기 / 접기", expanded=False):
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

    st.markdown("---")

    col_left, col_right = st.columns([1, 2.5])

    with col_left:
        st.subheader("⚙️ Control & Analytics")
        
        if st.button("▶️ 관람객 동선 시뮬레이션 실행"):
            st.session_state.simulating = True

        st.write("")
        st.metric(label="평균 혼잡도 (Density)", value="68%", delta="-5% (최적화됨)")
        st.metric(label="최대 정체 구역", value="Main Stage")
        st.metric(label="수용 가능 관람객 수", value="2,500 명")
        
        st.info("💡 **AI 제안**\nEntrance 인근 정체를 방지하기 위해 Photo Zone을 좌측 상단으로 분산 배치를 권장합니다.")

    with col_right:
        st.subheader("🗺️ Live Simulation Canvas")
        
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(10, 6), facecolor='#0f172a')
        ax.set_facecolor('#1e293b')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')
        ax.grid(True, color='#334155', linestyle='--', alpha=0.5)

        # 구역 그린 렌더링
        for name, item in st.session_state.layout.items():
            rect = plt.Rectangle(
                (item["x"] - item["w"]/2, item["y"] - item["h"]/2),
                item["w"], item["h"],
                facecolor=item["color"], edgecolor='white', alpha=0.6, linewidth=1.5
            )
            ax.add_patch(rect)
            ax.text(item["x"], item["y"], name, ha='center', va='center', 
                    fontweight='bold', color='white', fontsize=11)

        # 관람객 시뮬레이션
        num_particles = 120
        ent = st.session_state.layout["Entrance"]
        px = ent["x"] + np.random.uniform(-ent["w"]/3, ent["w"]/3, num_particles)
        py = ent["y"] + np.random.uniform(-ent["h"]/3, ent["h"]/3, num_particles)
        
        targets = [st.session_state.layout["Main Stage"], 
                   st.session_state.layout["Photo Zone"], 
                   st.session_state.layout["Food Zone"]]
        
        target_idx = np.random.choice(len(targets), size=num_particles, p=[0.5, 0.3, 0.2])
        tx = np.array([targets[i]["x"] for i in target_idx])
        ty = np.array([targets[i]["y"] for i in target_idx])

        if st.session_state.simulating:
            step = np.random.uniform(0.1, 0.8, num_particles)
            px = px + (tx - px) * step
            py = py + (ty - py) * step
            st.session_state.simulating = False

        ax.scatter(px, py, c='#f43f5e', s=25, alpha=0.8, edgecolors='white', linewidths=0.5, label='Attendees')
        
        # Heatmap
        x_grid, y_grid = np.meshgrid(np.linspace(0, 10, 80), np.linspace(0, 10, 80))
        z_density = np.zeros_like(x_grid)
        for x_p, y_p in zip(px, py):
            dist = np.sqrt((x_grid - x_p)**2 + (y_grid - y_p)**2)
            z_density += np.exp(-dist**2 / 0.8)
        
        ax.imshow(z_density, extent=[0, 10, 0, 10], origin='lower', cmap='YlOrRd', alpha=0.3)
        ax.legend(loc='upper left')

        st.pyplot(fig)

    # 하단 채팅창
    user_input = st.chat_input("공간 구조를 변경해보세요 (예: 무대 크게 해줘, 입구 더 넓혀줘)")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        response_text = "요청사항을 분석하여 레이아웃을 업데이트했습니다."
        
        if "무대" in user_input and ("크게" in user_input or "확장" in user_input):
            st.session_state.layout["Main Stage"]["w"] = 3.5
            response_text = "Main Stage 규모를 키워 관람 인원을 추가 수용할 수 있게 조정했습니다."
        elif "포토존" in user_input:
            st.session_state.layout["Photo Zone"]["x"] = 2.5
            st.session_state.layout["Photo Zone"]["y"] = 7.5
            response_text = "Photo Zone 위치를 이동시켰습니다."
        elif "입구" in user_input:
            st.session_state.layout["Entrance"]["w"] = 3.0
            response_text = "Entrance 폭을 넓혀 이동 동선을 원활하게 넓혔습니다."

        st.session_state.messages.append({"role": "assistant", "content": response_text})
        st.rerun()

# ---------------------------------------------------------
# PAGE 3: 📑 AI 보고서 생성
# ---------------------------------------------------------
elif st.session_state.current_page == "📑 AI 보고서 생성":
    st.title("📑 AI Venue Design & Safety Report")
    st.caption("현재 공간 레이아웃 기반 동선 및 안전도 진단 AI 보고서")
    st.markdown("---")

    col_btn, col_blank = st.columns([1, 2])
    with col_btn:
        generate_btn = st.button("✨ 실시간 AI 안전 보고서 생성하기")

    if generate_btn:
        with st.spinner("AI가 공간 시뮬레이션 데이터를 진단하고 보고서를 생성 중입니다..."):
            st.subheader("📋 행사장 공간 진단 최종 보고서")
            
            st.markdown("""
            ### 1. 종합 평가 및 점수
            * **안전도 점수:** `88/100` (우수)
            * **동선 효율성:** `B+ Grade`
            * **권장 최대 관람객 수:** `2,500명`

            ---

            ### 2. 구역별 분석 결과
            * **Main Stage (주 무대):** 전체 인원의 약 50%가 집중되는 고밀도 위험 구역입니다. 무대 전면 좌우측에 비상 통로 확보가 완비되었습니다.
            * **Entrance (입구):** 현재 진입로 폭 기준 시간당 약 800명 순탄한 입출장이 가능합니다.
            * **Photo Zone & Food Zone:** 관람객 머무름 시간이 긴 지역으로, 두 공간의 간격이 적절히 유지되고 있습니다.

            ---

            ### 3. AI 최종 가이드라인 및 조치사항
            1. **병목 완화:** 행사 시작 1시간 전, 입구 주변 펜스 설치를 권장합니다.
            2. **비상 동선:** Food Zone 측면에 비상 구급차 대기 구역 표시를 추가하세요.
            """)
            
            st.success("보고서 작성이 완료되었습니다.")
            st.download_button(
                label="📥 보고서 텍스트 파일 다운로드",
                data="[VIBE Space Report]\n안전도 점수: 88/100\n권장 수용인원: 2500명\n최종 조치: 비상 통로 확보 완료",
                file_name="VIBE_Space_Report.txt",
                mime="text/plain"
            )

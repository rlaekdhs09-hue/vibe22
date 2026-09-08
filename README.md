# VIBE SPACE DESIGNER v3
AI와 채팅하면서 행사장을 점진적으로 설계하는 Streamlit 프로토타입입니다.

- 최초 입력: 이벤트 이름 / 목적 / 방문객 수 / 예산 / 장소
- 빈 설계 보드에서 시작
- 자연어 채팅으로 공간 추가 및 간단한 수정
- 방문객 이동 동선 시각화
- 시간대별 혼잡도 Heatmap
- 회원가입 / 로그인

GitHub에 `app.py`, `requirements.txt`, `README.md`, `.gitignore`를 올린 뒤 Streamlit Cloud에서 `app.py`를 Main file로 선택하세요.

혼잡도는 실제 센서 데이터가 아닌 기획 단계의 추정 시각화입니다. 현재 채팅 해석도 외부 LLM API 없이 동작하는 프로토타입이며, 실제 서비스에서는 LLM과 DB를 연결해 확장할 수 있습니다.

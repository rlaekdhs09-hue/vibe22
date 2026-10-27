# Event Architect AI — Dashboard Development Specification

## 1. Project Overview

Build a fully functional, premium-quality web application dashboard for **Event Architect AI**, an AI-powered inclusive event planning platform.

**Product slogan:**
"AI가 모두가 함께 즐길 수 있는 행사를 설계합니다."

The application helps event organizers design safer, more accessible, and more efficient event venues by analyzing event information, generating venue layouts, simulating crowd movement, and presenting optimization results.

This project is intended for a Korean AI/SW competition. The final product must look like a realistic, professionally developed SaaS application rather than a static prototype or an AI-generated mockup.

### Primary objective

Implement the dashboard screen only.

Do not build separate full pages for Event Design, Digital Twin, Simulation, AI Report, or Settings. These can appear in the sidebar as navigation items, but the primary deliverable is a fully functional main dashboard.

The dashboard must be interactive. Buttons, inputs, filters, tabs, charts, and comparison controls must perform meaningful actions.

Do not merely create a screenshot-like interface.

---

## 2. Technology Stack

Use the following technologies:

* React
* TypeScript
* Vite
* Tailwind CSS
* Lucide React for icons
* Recharts for charts
* Three.js or React Three Fiber only if it materially improves the venue visualization

Use stable, compatible package versions.

Prefer lightweight, maintainable implementations. Avoid unnecessary dependencies.

Use local mock data and deterministic simulation logic where external services are unavailable.

Do not require paid APIs, external API keys, or a cloud account to run the application.

The application must start locally using standard npm commands.

---

## 3. Design Direction

Create a premium enterprise SaaS dashboard inspired by the visual quality of Linear, Stripe, Notion, Apple, and modern Figma products.

The interface must feel like a real product designed by an experienced professional UI/UX team.

### Visual identity

* Primary background: #F7F9FC
* Main surface: #FFFFFF
* Primary navy: #0F172A
* Primary blue: #2563EB
* Success green: #10B981
* Warning orange: #F59E0B
* Danger red: #EF4444
* Primary text: #111827
* Secondary text: #64748B
* Borders: #E5E7EB

Use a restrained color palette. Blue is the main interaction color, while green, orange, and red indicate meaningful status differences.

### Typography

Use Pretendard or another clean Korean sans-serif font with an appropriate fallback.

Maintain a clear typographic hierarchy:

* Page title: 26–30px
* Section title: 16–20px
* Card title: 13–15px
* Body text: 13–14px
* Supporting labels: 11–12px

Avoid excessively large headings, oversized cards, excessive gradients, glassmorphism, and decorative animations.

### Layout

Use a fixed desktop sidebar and a flexible main content area.

The initial target resolution is 1440 × 900, but the application must also work on smaller laptops, tablets, and mobile devices.

Use consistent spacing, subtle borders, restrained shadows, and carefully aligned components.

The interface must not feel crowded.

---

## 4. Global Application Layout

### A. Left sidebar

Create a fixed, white sidebar approximately 240px wide on desktop.

At the top, display:

**Event Architect AI**

Use a minimal geometric event or layout icon.

Below the logo, show these navigation items:

1. 대시보드
2. 이벤트 디자인
3. 디지털 트윈
4. AI 시뮬레이션
5. AI 리포트
6. 설정

Use Lucide icons and a consistent icon size.

The active Dashboard item should have a subtle blue background, blue icon, and stronger text weight.

At the bottom, display:

* A small project status indicator
* "AI 설계 엔진 준비 완료"
* A compact user profile area

The other navigation items may display an informative placeholder or a "준비 중" state when clicked. Do not create broken routes.

### B. Top header

The main content area must begin with a clean header containing:

* Breadcrumb: "Event Architect AI / 대시보드"
* A compact search or project selector
* Notification icon
* User avatar or initials

Keep the header visually lightweight.

### C. Main dashboard heading

Display:

**행사 설계 대시보드**

Supporting text:

"행사 데이터를 분석하고, 모두를 위한 최적의 행사 환경을 설계하세요."

On the right side, display:

* "마지막 업데이트" with a realistic timestamp
* A primary button: "+ 새 행사 만들기"

Clicking the button should open a functional modal or form for creating a new event.

---

## 5. Event Input and Design Controls

Create a prominent event configuration card near the top of the dashboard.

The card title is:

**행사 설계 조건**

Supporting text:

"행사 정보를 입력하면 AI가 조건에 맞는 설계안을 생성합니다."

Include the following fields:

### Event name

Default value: "2026 교내 과학축제"

### Event venue

Provide selectable venue types:

* 학교 운동장
* 실내 체육관
* 공원
* 전시장
* 사용자 지정 공간

### Event purpose

Use selectable chips or a segmented control:

* 안전 중심
* 참여 중심
* 운영 효율
* 예산 효율

The selected purpose must visibly affect the simulation scoring weights.

### Expected visitors

Numeric input with a sensible default of 1,500.

Validate that the value is a positive integer.

### Budget

Numeric input with a default of 5,000,000 KRW.

Display formatted Korean currency.

### Event duration

Allow users to select the start and end times or choose a duration in hours.

### Booth configuration

Allow users to specify:

* Number of experience booths
* Number of food booths
* Number of performance stages
* Number of rest areas

### Required facilities

Provide selectable checkboxes for:

* 무대
* 푸드존
* 체험부스
* 휴게공간
* 화장실
* 안내센터
* 응급의료센터
* 휠체어 이동 경로

### Main action

Create a prominent button:

**AI 행사 설계 시작**

The button must validate the input fields before running the simulation.

Display helpful Korean validation messages next to invalid fields.

Do not navigate away from the dashboard.

---

## 6. Main Venue Visualization

This is the visual centerpiece of the dashboard.

Create a large venue map card titled:

**AI 행사장 디지털 트윈**

Supporting label:

"행사장 배치 및 예상 방문객 이동 경로"

The visualization should occupy approximately 55–60% of the main dashboard's central content width.

### Venue map requirements

Create a polished, top-down or slightly isometric 2D venue visualization.

Use SVG, Canvas, or a lightweight drawing implementation if a full 3D scene would add unnecessary complexity.

The venue should resemble a real event venue, not a game map.

Display distinct, clearly labeled facility blocks:

* 무대
* 푸드존
* 체험부스
* 휴게공간
* 안내센터
* 응급의료센터
* 화장실
* 주 출입구
* 비상 출구

Use realistic spatial relationships, consistent proportions, clear pathways, and sufficient spacing between facilities.

The venue must be legible at normal desktop viewing size.

### Crowd movement

Represent visitors as small, restrained dots or grouped markers.

Use blue and orange markers to distinguish different simulated visitor groups.

Draw directional paths with SVG arrows or lines.

Show congestion through a semi-transparent heatmap:

* Green: low congestion
* Yellow: moderate congestion
* Orange: high congestion
* Red: critical congestion

Do not cover all facility labels with the heatmap.

Add a compact legend explaining the colors.

### Map controls

Include:

* 전체 보기
* 혼잡도
* 이동 동선
* 접근성
* 대피 경로

These controls must switch the displayed visualization layer.

Add zoom-in, zoom-out, and reset-view controls if practical.

Clicking a facility should open a small detail panel showing its type, estimated visitors, accessibility status, and congestion level.

### Before/After comparison

Provide a functional toggle:

* 기존 배치
* AI 최적화 배치

Switching the toggle must change the venue layout and relevant metrics.

The initial demonstration should visibly show improvements without suggesting that simulated results are real-world guarantees.

---

## 7. AI Analysis Panel

Create a dedicated analysis panel on the right side of the main venue visualization.

Title:

**AI 설계 분석**

Show five compact metric cards or rows.

### Metrics

1. 안전성 점수
2. 접근성 점수
3. 동선 효율성
4. 예상 대기시간
5. 예산 효율성

Use plausible sample values for the initial demonstration.

For example:

* 안전성: 94/100
* 접근성: 96/100
* 동선 효율성: 91/100
* 예상 대기시간: 8분
* 예산 효율성: 89/100

Use progress bars, small indicators, or restrained visualizations.

Avoid oversized circular gauges.

Clearly label the values as example simulation results until the user runs a simulation.

Do not claim that these metrics are scientifically validated or represent actual safety certification.

### Overall design score

Display:

**종합 설계 점수**

Show a score out of 100 and a short explanation of the main strengths and weaknesses.

The overall score must be calculated from the underlying metric values rather than hardcoded independently.

Use the selected event purpose to adjust the weighting of the metrics.

---

## 8. AI Recommendations

Create a card titled:

**AI 개선 권장 사항**

Display three to five recommendations generated from the current simulation data.

Example recommendations:

* 푸드존을 남쪽으로 이동하여 주요 통로의 혼잡을 줄이세요.
* 휴게공간을 추가해 이동 중 휴식이 필요한 방문객의 편의를 높이세요.
* 주 출입구 주변의 부스 간격을 넓혀 병목 가능성을 낮추세요.
* 안내센터를 중앙 동선과 가까운 위치로 이동하세요.
* 휠체어 이동 경로가 모든 주요 시설에 연결되는지 확인하세요.

Each recommendation should contain:

* Recommendation title
* Reason
* Expected effect
* A relevant priority indicator

Whenever practical, provide an action button such as:

"배치에 적용"

Clicking this button must update the venue layout and recalculate the affected metrics.

Recommendations should be derived from the simulation state. Avoid randomly generating unrelated suggestions.

---

## 9. Crowd and Operations Analytics

Create a compact analytics section below the venue map.

Include:

### A. Hourly visitor distribution

Use Recharts to create a clean line or area chart.

Title:

"시간대별 예상 방문객"

Use a realistic demonstration dataset.

Allow the user to switch between visitor volume and congestion indicators.

### B. Facility congestion

Create a horizontal bar chart showing estimated congestion by location.

Example locations:

* 무대 입구
* 푸드존
* 체험부스
* 주 출입구
* 안내센터

### C. Before/After comparison

Compare the original layout and the optimized layout using the same metrics.

Display:

* 예상 혼잡도
* 평균 이동거리
* 예상 대기시간
* 접근성 점수

Use percentage changes only when calculated from the underlying values.

Always distinguish between simulated estimates and measured real-world data.

---

## 10. Functional AI Simulation

Implement a locally runnable, deterministic simulation engine.

Do not merely animate a loading spinner and return fixed values.

The simulation should use the current user inputs to calculate results.

### Simulation sequence

When the user clicks "AI 행사 설계 시작":

1. Validate all input fields.
2. Display a simulation progress panel.
3. Show the stages:

   * 입력 조건 분석
   * 행사장 배치안 생성
   * 방문객 이동 시뮬레이션
   * 혼잡도 및 접근성 평가
   * 최적 설계안 선정
4. Generate a set of candidate layouts using deterministic rules and controlled variations.
5. Evaluate each candidate using measurable criteria.
6. Select the candidate with the best score for the current event purpose.
7. Update the venue map, analysis panel, recommendations, and comparison charts.
8. Display a concise summary of the changes.

Use an appropriate number of candidate layouts for responsive local execution.

Do not claim that thousands of layouts were actually simulated if the application evaluates only a smaller number.

If the interface displays a candidate count, it must reflect the actual number processed.

### Optimization criteria

Use a multi-objective scoring function incorporating:

* Safety and congestion
* Accessibility
* Walking distance
* Queue estimates
* Visitor distribution
* Budget constraints

The scoring function must be transparent and understandable.

Different event purposes must produce different scoring weights.

For example, safety-focused events should prioritize congestion and evacuation-path availability, while participation-focused events should prioritize access to booths and balanced visitor distribution.

The result should be reproducible for identical inputs.

Clearly state that this is a prototype simulation based on simplified assumptions, not a validated crowd-safety model.

---

## 11. Data Persistence

Use localStorage for lightweight persistence.

Save:

* Current event configuration
* Latest simulation results
* Selected visualization layer
* Recent events
* User interface preferences

Refresh the page without losing the current demonstration state.

Provide a reset or clear-demo-data option.

Keep simulation logic separate from presentation components.

Use TypeScript interfaces for event configuration, venue facilities, simulation results, metric scores, and recommendations.

Avoid putting the entire application in one component.

---

## 12. Responsive Design

### Desktop

* Fixed left sidebar
* Event configuration at the top
* Large venue map in the center
* Analysis and recommendation panel on the right
* Analytics section below

### Tablet

* Collapsible sidebar
* Two-column layout where space permits
* Stack the map and analysis panel when necessary

### Mobile

* Sidebar becomes a compact drawer or bottom navigation
* Event inputs stack vertically
* Venue map remains usable without horizontal page overflow
* Metrics become compact cards
* Charts resize to fit the viewport
* Buttons remain large enough to tap
* Tables and labels must not overflow their containers

Do not simply shrink the desktop interface. Design a proper mobile layout.

---

## 13. Accessibility and Localization

The application must be in Korean by default.

Use Korean for:

* Navigation
* Page titles
* Field labels
* Buttons
* Validation messages
* Recommendations
* Charts
* Status indicators
* Empty states
* Tooltips

Keep technical product names such as Event Architect AI and API when appropriate.

Use semantic HTML, keyboard-accessible controls, visible focus indicators, and sufficient color contrast.

Do not rely on color alone to communicate congestion or status.

---

## 14. Code Quality and Architecture

Use reusable React components.

Suggested component structure:

* AppShell
* Sidebar
* DashboardHeader
* EventConfigurationForm
* VenueDigitalTwin
* VenueFacility
* MapLayerControls
* AIAnalysisPanel
* MetricCard
* AIRecommendationList
* VisitorFlowChart
* CongestionBarChart
* BeforeAfterComparison
* SimulationProgressModal

Separate the simulation and optimization logic into dedicated TypeScript modules.

Avoid duplicated logic and hardcoded UI values where they should be calculated.

Include reasonable error handling and empty states.

Ensure that all buttons and interactive controls have meaningful behavior.

Do not use fake links, dead buttons, or controls that only change their visual appearance without affecting the application.

---

## 15. Final Quality Requirements

The final application must:

* Run locally without paid services.
* Build successfully without TypeScript errors.
* Display a complete Korean dashboard.
* Include a realistic venue map.
* Support event information input.
* Run a deterministic simulation based on the inputs.
* Update metrics and recommendations after simulation.
* Support before/after comparison.
* Include working visualization controls.
* Persist the demonstration state locally.
* Work on desktop and mobile.
* Use consistent spacing, typography, colors, and iconography.
* Contain no broken images, missing icons, or overflowing components.
* Avoid unnecessary decorative gradients and excessive animations.

Do not stop after generating the initial UI.

After implementation, run the application, inspect the dashboard, test the main interactions, fix errors, and verify the production build.

The final result should be suitable for a live demonstration at a national AI/SW competition.

**Priority order:**

1. Functional correctness
2. Clear demonstration of the AI event-design concept
3. Premium visual quality
4. Responsive layout
5. Maintainable code

Deliver the complete working project, not just a design description or static mockup.

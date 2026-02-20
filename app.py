import streamlit as st
import pandas as pd
import plotly.express as px # 차트용 (설치 안됐으면 pip install plotly 필요)
import time

# --- 1. 데이터 베이스 (실무 데이터 기반) ---
PROHIBITED_TERMS = {
    "밧데리": "배터리",
    "운전사": "운전자(드라이버)",
    "기름차": "내연기관차",
    "전기차": "전동화 모델(EV)",
    "자율주행 3단계": "레벨 3 자율주행",
    "고급": "프리미엄/럭셔리"
}

# --- 2. 스타일링 ---
st.set_page_config(page_title="HMG Journal Advanced Suite", layout="wide")
st.markdown("""
    <style>
    .report-card { background-color: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #ddd; color: #111; }
    .highlight { color: #ff4b4b; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 메인 기능 로직 ---
st.title("🚗 HMG Journal Workflow AI v5.0")

tab1, tab2, tab3 = st.tabs(["✍️ 지능형 원고 검안", "💬 클라이언트어 실전번역", "🎨 비주얼 가이드"])

with tab1:
    col_input, col_result = st.columns([1, 1])
    
    with col_input:
        st.subheader("원고 분석 엔진")
        category = st.selectbox("콘텐츠 카테고리", ["기술 심화", "WRC/N", "신차 시승기", "브랜드 캠페인"])
        draft = st.text_area("초안을 입력하세요", height=400, placeholder="여기에 분석할 내용을 입력하세요.")
        run_analysis = st.button("HMG 톤앤매너 검밀 실행")

    with col_result:
        if run_analysis and draft:
            with st.spinner("AI가 HMG 가이드라인에 맞춰 분석 중..."):
                time.sleep(1.5)
                
                # 가상 점수 계산
                score_data = {
                    '항목': ['전문성', '역동성', '브랜드톤', '가독성', '기술깊이'],
                    '점수': [80, 45, 70, 55, 90]
                }
                
                # 1. 레이더 차트 (와우 포인트)
                fig = px.line_polar(score_data, r='점수', theta='항목', line_close=True, range_r=[0,100])
                fig.update_traces(fill='toself', line_color='#002c5f')
                st.plotly_chart(fig, use_container_width=True)
                
                # 2. 실시간 용어 검사 (실용성 포인트)
                st.markdown("#### 🔍 실시간 용어 교정")
                found_errors = []
                for wrong, right in PROHIBITED_TERMS.items():
                    if wrong in draft:
                        found_errors.append(f"- <span class='highlight'>{wrong}</span> → **{right}**")
                
                if found_errors:
                    for error in found_errors:
                        st.markdown(error, unsafe_allow_html=True)
                else:
                    st.success("✅ 표준 용어 위반 사항이 없습니다.")
                    
                # 3. 클로드용 프롬프트 자동 생성
                st.markdown("#### 🤖 최적화된 프롬프트")
                st.code(f"Role: HMG 저널 수석 에디터\nTask: {category}에 맞춰 다음 원고를 윤문하라.\nGoal: 역동성을 20% 높이고 전문 용어를 적절히 배치할 것.\nContent: {draft[:100]}...")

with tab2:
    st.subheader("💬 클라이언트어 리얼 번역")
    # 좀 더 실무적인 예시들
    examples = {
        "임팩트가 부족해요": "메인 썸네일에 차량의 속도감이 느껴지는 모션 블러 효과를 넣고, 제목에 '최초'라는 단어를 쓰세요.",
        "조금 더 럭셔리하게": "채도를 낮추고 폰트 자간을 넓히세요. 여백을 평소보다 1.5배 더 잡으세요.",
        "N의 감성을 살려주세요": "팝앤뱅 사운드 묘사를 의성어로 넣고, 배경색에 퍼포먼스 블루(#659ad2)를 활용하세요."
    }
    selected_ex = st.selectbox("자주 듣는 '답답한' 요청들:", list(examples.keys()))
    if st.button("속마음 분석"):
        st.info(f"🎯 **실제 수정 방향:** {examples[selected_ex]}")

with tab3:
    st.subheader("🎬 AI 비주얼 디렉팅")
    st.write("이미지 한 장으로 뽑아내는 숏폼/영상 기획안")
    img = st.file_uploader("차량 사진을 업로드하면 영상 구도를 제안합니다 (데모)")
    if img:
        st.image(img, width=400)
        st.success("🎥 분석 결과: 팬닝 샷(Panning Shot) 추천. 배경을 흐리게 처리하여 속도감 극대화 필요.")

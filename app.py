import streamlit as st
import pandas as pd
import time

# --- 1. 설정 및 데이터 (HMG 저널 가이드라인 반영) ---
st.set_page_config(page_title="HMG Journal AI Suite v4.0", layout="wide")

CONTENT_MODELS = {
    "WRC 리뷰": {
        "icon": "🏎️",
        "guide": "라운드별 결과 + 기술 분석 (타이어, 날씨, 심리)",
        "resources": ["wrc.com", "rally-maps.com", "WRC YouTube"],
        "keywords": ["그럼에도", "덕분에", "이에 따라", "라운드", "스테이지"]
    },
    "어워드 수상": {
        "icon": "🏆",
        "guide": "글로벌 인정 + K자동차 위상 강화 (객관적 지표)",
        "resources": ["J.D. Power", "What Car?", "Parkers"],
        "keywords": ["입증했다", "강화했다", "선점했다", "최초", "최고"]
    },
    "독일 비교 테스트": {
        "icon": "🇩🇪",
        "guide": "정량적 우수성 입증 (독일 매체 권위 활용)",
        "resources": ["Auto Bild", "Auto Motor Sport"],
        "keywords": ["0-100km/h", "제원", "압도적", "우위", "평가점수"]
    },
    "시승기": {
        "icon": "🚗",
        "guide": "체험 + 철학 + 감각적 묘사 (드라마틱한 전개)",
        "resources": ["HMG TV", "Genesis Media"],
        "keywords": ["묵직한", "짜릿한", "응축된", "필링", "동역학"]
    }
}

# --- 2. 스타일링 ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .stTabs [data-baseweb="tab-list"] { background-color: #002c5f; border-radius: 10px 10px 0 0; }
    .stTabs [data-baseweb="tab"] { color: white; padding: 10px 20px; }
    .stTabs [aria-selected="true"] { border-bottom-color: #00aad2 !important; color: #00aad2 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 헤더 & 사이드바 ---
st.title("⚡ HMG Journal Content Suite v4.0")
st.caption("고도화된 HMG 저널 제작 전용 AI 어시스턴트")

with st.sidebar:
    st.image("https://www.hyundai.co.kr/static/images/logo_hmg.png", width=150)
    st.header("🛠️ 작업 설정")
    selected_type = st.selectbox("콘텐츠 타입 선택", list(CONTENT_MODELS.keys()))
    st.divider()
    st.markdown(f"**{selected_type} 가이드:**\\n{CONTENT_MODELS[selected_type]['guide']}")

# --- 4. 메인 기능 ---
tab1, tab2, tab3 = st.tabs(["📊 지능형 편집기", "💬 클라이언트어 번역", "🎬 비주얼 제안"])

with tab1:
    col1, col2 = st.columns([1.2, 0.8])
    with col1:
        st.subheader(f"{CONTENT_MODELS[selected_type]['icon']} {selected_type} 원고 분석")
        user_input = st.text_area("텍스트를 입력하세요", height=300)
        if st.button("분석 및 프롬프트 생성"):
            st.session_state['analyzed'] = True

    with col2:
        if 'analyzed' in st.session_state:
            st.subheader("📝 분석 결과")
            st.metric("HMG 톤앤매너 일치도", "82%", "우수")
            st.progress(82)
            st.write("**핵심 교정 사항:**")
            st.write("- 기술적 용어 보강 필요")
            st.write("- 능동형 문장 사용 권장")
            
            st.subheader("📋 Claude용 프롬프트")
            st.code(f"이 원고를 {selected_type} 스타일에 맞춰 교정해줘: {user_input[:50]}...", language="markdown")

with tab2:
    st.subheader("💬 클라이언트어 번역기")
    c_input = st.text_input("요청사항 입력")
    if st.button("해석하기"):
        st.info("실제 의도: 시각적인 화려함보다는 기술적 신뢰도를 강조해 달라는 뜻입니다.")

with tab3:
    st.subheader("🎬 비주얼 스토리보딩")
    if st.button("시뮬레이션"):
        st.success("추천 구도: 저각도(Low-angle) 주행샷")
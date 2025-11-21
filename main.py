import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 추천기",
    page_icon="🎯",
    layout="centered"
)

# --- 상단 타이틀 ---
st.markdown(
    """
    <h1 style="text-align:center;">🎯 MBTI 기반 진로 추천기</h1>
    <p style="text-align:center; font-size:18px;">너의 성격 유형으로 찾는 최적의 커리어✨</p>
    """,
    unsafe_allow_html=True
)

# --- MBTI 목록 ---
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# --- MBTI별 진로 추천 데이터 ---
career_map = {
    "INTJ": ["데이터 사이언티스트 📊", "전략기획 전문가 🎯", "AI 연구원 🤖"],
    "INTP": ["연구원 🔬", "시스템 엔지니어 🛠️", "이론 물리학자 🌌"],
    "ENTJ": ["경영 컨설턴트 💼", "프로덕트 매니저 🚀", "창업가 🔥"],
    "ENTP": ["혁신 전략가 💡", "벤처 창업가 🚀", "크리에이티브 디렉터 🎨"],

    "INFJ": ["상담사 🧠", "교육 전문가 📚", "콘텐츠 기획자 ✍️"],
    "INFP": ["작가 ✒️", "심리 상담가 🧘‍♂️", "예술가 🎨"],
    "ENFJ": ["HR 전문가 🤝", "교육 코치 📘", "비영리 단체 활동가 🌱"],
    "ENFP": ["마케터 📣", "크리에이터 🎥", "브랜드 전문가 ⭐"],

    "ISTJ": ["공무원 🏛️", "품질관리 전문가 📏", "회계사 📑"],
    "ISFJ": ["간호사 🏥", "행정 전문가 🗂️", "보건·복지 분야 종사자 ❤️"],
    "ESTJ": ["프로젝트 매니저 📋", "경영 관리자 🧷", "군 장교 🎖️"],
    "ESFJ": ["교사 🍎", "서비스 매니저 🎧", "사회복지사 🤲"],

    "ISTP": ["정비사 🔧", "보안 전문가 🔐", "영상·음향 엔지니어 🎧"],
    "ISFP": ["디자이너 🎨", "플로리스트 🌸", "뮤지션 🎵"],
    "ESTP": ["세일즈 전문가 💼", "이벤트 플래너 🎉", "응급 구조 대원 🚑"],
    "ESFP": ["연예인 ⭐", "엔터테인먼트 기획자 🎤", "여행 코디네이터 ✈️"]
}

# --- 사용자 입력 ---
selected_mbti = st.selectbox("📌 MBTI를 선택하세요", mbti_types)

st.markdown("---")

# --- 추천 결과 출력 ---
if selected_mbti:
    st.markdown(f"### 🔍 {selected_mbti} 유형에게 어울리는 진로")
    careers = career_map[selected_mbti]

    for idx, c in enumerate(careers, 1):
        st.markdown(f"**{idx}. {c}**")

    st.markdown("---")
    st.success("✨ 너의 성향을 살린 커리어를 찾아보는 중! 본격적으로 탐색해보자!")


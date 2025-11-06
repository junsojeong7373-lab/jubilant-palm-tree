# app.py
# Streamlit 앱: MBTI별 진로 추천
# 실행: streamlit run app.py
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천 💡", page_icon="🧭", layout="centered")

# 제목과 설명
st.title("MBTI로 보는 추천 진로 🧭✨")
st.caption("네 MBTI 골라봐! 유형별로 어울리는 진로 2가지를 추천해줄게 💬")

# MBTI별 진로 데이터
MBTI_DATA = {
    "ISTJ": [
        {"career": "공무원 🏛️", "majors": "행정학, 법학, 경영학", "personality": "꼼꼼하고 책임감 강함. 규칙과 절차를 잘 따르는 편."},
        {"career": "회계사 / 세무사 📊", "majors": "회계학, 경영학, 경제학", "personality": "숫자에 강하고 정확성을 중시하는 성격."},
    ],
    "ISFJ": [
        {"career": "간호사 🩺", "majors": "간호학, 보건학", "personality": "배려심 많고 인내심이 강함. 사람 돌보는 걸 좋아함."},
        {"career": "사회복지사 🤝", "majors": "사회복지학, 상담학", "personality": "타인의 필요에 민감하고 실용적 도움을 제공하는 성향."},
    ],
    "INFJ": [
        {"career": "상담사 / 심리치료사 💬", "majors": "심리학, 교육학, 상담학", "personality": "통찰력 있고 깊은 공감 능력을 지님."},
        {"career": "교육자 / 연구자 📚", "majors": "교육학, 인문·사회계열, 심리학", "personality": "이상과 비전을 중시하며 사람을 이끄는 성향."},
    ],
    "INTJ": [
        {"career": "연구원 / 데이터 사이언티스트 🔬", "majors": "수학, 통계학, 컴퓨터공학", "personality": "전략적이고 분석적. 혼자 집중해서 일하기 좋아함."},
        {"career": "전략 컨설턴트 📈", "majors": "경영학, 경제학, 통계학", "personality": "체계적 사고와 문제해결 능력이 뛰어남."},
    ],
    "ISTP": [
        {"career": "기계·전기 엔지니어 ⚙️", "majors": "기계공학, 전기·전자공학", "personality": "실용적이고 손으로 직접 만드는 걸 좋아함. 문제 즉시 해결하는 스타일."},
        {"career": "응급구조사 / 소방관 🚒", "majors": "응급구조학, 소방학, 보건계열", "personality": "위기 상황에서 침착하고 행동력이 빠름.

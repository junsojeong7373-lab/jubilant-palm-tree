# app.py
# Streamlit 앱: MBTI별 진로 추천 (16개 유형)
# 실행: streamlit run app.py
import streamlit as st

st.set_page_config(page_title="MBTI 진로 추천 💡", page_icon="🧭", layout="centered")

# 제목과 간단 설명
st.title("MBTI로 보는 추천 진로 🧭✨")
st.caption("네 MBTI 골라봐! 유형별로 어울리는 진로 2가지를 추천해줄게. (친근한 톤 + 이모지 포함)")

# MBTI 데이터: 각 유형에 대해 진로 2개, 적합 학과, 적합 성격 설명
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
        {"career": "상담사 / 심리치료사 💬", "majors": "심리학, 교육학, 상담학", "personality": "통찰력이 있고 깊은 공감 능력을 지님."},
        {"career": "교육자 / 연구자 📚", "majors": "교육학, 인문·사회계열, 심리학", "personality": "이상과 비전을 중시하며 사람을 이끄는 성향."},
    ],
    "INTJ": [
        {"career": "연구원 / 데이터 사이언티스트 🔬", "majors": "수학, 통계학, 컴퓨터공학, 전공 연구분야", "personality": "전략적이고 분석적. 혼자 집중해서 일하기 좋아함."},
        {"career": "전략 컨설턴트 📈", "majors": "경영학, 경제학, 통계학", "personality": "체계적 사고와 문제해결 능력이 뛰어남."},
    ],
    "ISTP": [
        {"career": "기계·전기 엔지니어 ⚙️", "majors": "기계공학, 전기·전자공학", "personality": "실용적이고 손으로 직접 만드는 걸 좋아함. 문제 즉시 해결하는 스타일."},
        {"career": "응급구조사 / 소방관 🚒", "majors": "응급구조학, 소방학, 보건계열", "personality": "위기 상황에서 침착하고 행동력이 빠름."},
    ],
    "ISFP": [
        {"career": "디자이너 / 아티스트 🎨", "majors": "시각디자인, 산업디자인, 예술학", "personality": "감각적이고 창의적. 자유로운 표현을 좋아함."},
        {"career": "사진작가 / 영상편집자 📸", "majors": "미디어학, 영상학, 디자인", "personality": "감성적이고 순간을 포착하는 능력이 좋음."},
    ],
    "INFP": [
        {"career": "작가 / 콘텐츠 크리에이터 ✍️", "majors": "문예창작, 국문학, 미디어학", "personality": "상상력이 풍부하고 자기만의 세계를 표현하길 좋아함."},
        {"career": "인권·NGO 활동가 🌱", "majors": "사회학, 국제학, 인문계열", "personality": "가치 지향적이고 의미 있는 일을 추구함."},
    ],
    "INTP": [
        {"career": "소프트웨어 개발자 / 프로그래머 💻", "majors": "컴퓨터공학, 정보통신", "personality": "논리적이고 호기심이 많으며 추상적 문제를 좋아함."},
        {"career": "연구원 (기초과학) 🔎", "majors": "물리/수학/전산학 등 이공계", "personality": "이론을 깊게 파고드는 걸 즐김."},
    ],
    "ESTP": [
        {"career": "영업 / 이벤트 기획자 🎉", "majors": "경영학, 광고홍보, 마케팅", "personality": "행동력이 빠르고 사람 만나는 걸 즐김."},
        {"career": "파일럿 / 항공 정비사 ✈️", "majors": "항공운항, 항공정비", "personality": "모험심 있고 실전 감각이 좋음."},
    ],
    "ESFP": [
        {"career": "퍼포먼스 아티스트 / 배우 🎭", "majors": "연극영화과, 공연예술", "personality": "활발하고 사람 앞에서 빛나는 타입."},
        {"career": "호텔·서비스 매니저 🏨", "majors": "관광학, 호텔경영", "personality": "상황 대처가 빠르고 친화력 좋음."},
    ],
    "ENFP": [
        {"career": "마케터 / 브랜드 매니저 📣", "majors": "광고홍보, 경영학, 미디어", "personality": "창의적이고 아이디어가 풍부. 사람과 소통하는 걸 좋아함."},
        {"ca

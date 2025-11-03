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
        {"career": "스타트업 창업가 🚀", "majors": "경영학, 컴퓨터공학 등 다양", "personality": "열정적이고 새로운 시도를 두려워하지 않음."},
    ],
    "ENTP": [
        {"career": "제품 기획자 / UX 리서처 🧩", "majors": "산업공학, 디자인, 컴퓨터", "personality": "아이디어가 많고 토론을 즐기는 창의적 문제해결가."},
        {"career": "변호사 / 논리 기반 직업 ⚖️", "majors": "법학, 정치외교학", "personality": "말재주가 있고 논리적으로 상대를 설득하는 능력 우수."},
    ],
    "ESTJ": [
        {"career": "관리자 / 운영 매니저 🧑‍💼", "majors": "경영학, 산업공학", "personality": "조직을 이끄는 능력, 규칙 준수를 중시함."},
        {"career": "경찰 / 군무원 🚔", "majors": "경찰행정, 군사학, 행정학", "personality": "책임감 강하고 질서를 유지하는 걸 중요시함."},
    ],
    "ESFJ": [
        {"career": "교사 / 교육행정가 🍎", "majors": "교육학, 초등교육/특수교육", "personality": "사교적이고 다른 사람 돌보는 걸 좋아함."},
        {"career": "간호관리자 / 의료행정 🏥", "majors": "간호학, 보건행정", "personality": "현실적이고 협력적으로 일함."},
    ],
    "ENFJ": [
        {"career": "HR / 조직 개발가 🧑‍🤝‍🧑", "majors": "경영학, 심리학, 사회학", "personality": "사람을 이끄는 능력이 뛰어나며 동기부여에 강함."},
        {"career": "공공정책·사회운동가 🗳️", "majors": "정치외교, 사회학, 국제학", "personality": "비전 제시와 사람 모으는 데 뛰어남."},
    ],
    "ENTJ": [
        {"career": "CEO / 전략기획자 🏢", "majors": "경영학, 경제학, 산업공학", "personality": "리더십 강하고 목표 달성에 집중하는 타입."},
        {"career": "투자분석가 / 금융전문가 💹", "majors": "경제학, 수학, 통계학", "personality": "결단력 있고 큰 그림을 보는 능력."},
    ],
}

# MBTI 선택 UI
mbti_list = sorted(list(MBTI_DATA.keys()))
selected = st.selectbox("너의 MBTI를 골라줘 ➤", mbti_list, index=0)

# 결과 보여주기
st.markdown("---")
st.subheader(f"🧾 {selected} 유형을 위한 추천 진로")
choices = MBTI_DATA.get(selected, [])

for idx, info in enumerate(choices, start=1):
    st.markdown(f"### {idx}. {info['career']}")
    st.write(f"**어울리는 학과 / 전공**: {info['majors']}")
    st.write(f"**어울리는 성격**: {info['personality']}")
    st.write("")  # 공백

st.info("참고: MBTI는 성향을 알려주는 도구일 뿐, 진로를 100% 결정하지는 않아. 여러 경험을 해보고 너에게 맞는 길을 찾아봐! ✨")

# 추가 팁 토글
with st.expander("진로 고를 때 팁 보기 🌱"):
    st.write(
        "- 실제로 관심 있는 과목, 동아리, 체험활동을 먼저 해봐.  
- 직업인의 하루를 찾아보거나 멘토를 만나서 물어보는 게 큰 도움이 돼.  
- 전공과 직업은 완전히 일치하지 않아. 유연하게 생각하자!"
    )

st.caption("앱 만든이: 챗 · 더 많은 팁은 gptonline.ai/ko/ 참고해봐! 😉")

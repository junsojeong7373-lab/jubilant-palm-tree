# app.py
# -----------------------------
# 📊 2025년 10월 지역별 연령대 인구 그래프 (Plotly + Streamlit)
# 실행 방법:
# 1. Streamlit Cloud에 업로드
# 2. population.csv 파일 함께 올리기
# 3. streamlit run app.py
# -----------------------------

import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="2025년 인구 구조 분석", page_icon="📊", layout="centered")

# 제목
st.title("📊 2025년 10월 지역별 연령대 인구 시각화")

# CSV 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요 (예: population.csv)", type=["csv"])

if uploaded_file is not None:
    # 인코딩 자동 감지 시도
    try:
        df = pd.read_csv(uploaded_file, encoding="utf-8")
    except:
        try:
            df = pd.read_csv(uploaded_file, encoding="cp949")
        except:
            df = pd.read_csv(uploaded_file, encoding="euc-kr")

    # 숫자 컬럼 변환
    numeric_cols = [col for col in df.columns if "거주자" in col and "행정구역" not in col]
    for col in numeric_cols:
        df[col] = df[col].astype(str).str.replace(",", "").astype(int)

    # 지역 선택
    regions = df["행정구역"].unique().tolist()
    region = st.selectbox("📍 지역을 선택하세요:", regions)

    # 선택한 지역 데이터 필터링
    row = df[df["행정구역"] == region].iloc[0]
    data = pd.DataFrame({
        "연령대": numeric_cols[2:],  # 첫 2개는 총인구, 연령구간인구수
        "인구수": [row[col] for col in numeric_cols[2:]]
    })

    # 연령대 문자열 정리
    data["연령대"] = data["연령대"].str.extract(r"거주자_(.*)")[0]

    # Plotly 꺾은선 그래프
    fig = px.line(
        data,
        x="연령대",
        y="인구수",
        title=f"📈 {region} 연령대별 인구 분포 (2025년 10월)",
        markers=True,
    )
    fig.update_traces(line_color="#007BFF", marker=dict(size=8))
    fig.update_layout(
        xaxis_title="연령대",
        yaxis_title="인구수",
        template="plotly_white",
        hovermode="x unified",
    )

    st.plotly_chart(fig, use_container_width=True)

    # 요약 통계
    total_pop = row[numeric_cols[0]]
    st.info(f"✅ **{region} 총인구:** {int(total_pop):,}명")

else:
    st.warning("📂 CSV 파일을 업로드하면 그래프가 표시됩니다.")

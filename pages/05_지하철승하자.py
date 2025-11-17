# app.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="지하철 상위역(Top10) — 승차+하차 (Plotly)", layout="centered")

st.title("📊 지하철 상위 10개 역 (승차 + 하차 합) — 2025년 10월")
st.caption("날짜와 호선을 선택하면 해당 조건에서 승차+하차 합이 큰 역 상위 10개를 보여줍니다.")

@st.cache_data
def load_data(path: str):
    """
    데이터 로드: 한국 csv 특성(탭구분자, cp949)에 맞춰 안전하게 읽음.
    반환: 정리된 DataFrame (date: datetime, line, station, in_cnt, out_cnt, total)
    """
    # 먼저 시도: 탭으로 분리
    try:
        df = pd.read_csv(path, sep="\t", encoding="cp949", engine="python")
    except Exception as e:
        # fallback: 자동 구분자
        df = pd.read_csv(path, encoding="cp949", engine="python")
    
    # 컬럼 이름 정리 (공백/특수문자 제거)
    df.columns = [c.strip().lstrip("\ufeff") for c in df.columns]
    
    # 흔한 한국어 컬럼명들을 영어명으로 매핑 (파일이 다른 포맷이면 여기서 확장)
    # 예: '노선명' '역명' '승차총승객수' '하차총승객수' 또는 비슷한 이름
    col_map = {}
    for c in df.columns:
        if "노선" in c:
            col_map[c] = "line"
        elif "역" in c and "명" in c:
            col_map[c] = "station"
        elif "승차" in c:
            col_map[c] = "in_cnt"
        elif "하차" in c:
            col_map[c] = "out_cnt"
        elif any(x in c for x in ["일자","날짜","date"]):
            col_map[c] = "date_raw"
        elif c.lower().strip() in ["date","yyyymmdd"]:
            col_map[c] = "date_raw"
    df = df.rename(columns=col_map)
    
    # 만약 date_raw 컬럼이 없으면, 첫 컬럼이 날짜일 가능성 있음
    if "date_raw" not in df.columns:
        # 시도: 첫 컬럼 이름으로
        possible = df.columns[0]
        df = df.rename(columns={possible: "date_raw"})
    
    # 숫자형으로 변환 (in/out)
    for c in ["in_cnt", "out_cnt"]:
        if c in df.columns:
            # 숫자에 쉼표가 있을 수 있으므로 처리
            df[c] = df[c].astype(str).str.replace(",", "").str.strip()
            df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0).astype(int)
        else:
            # 컬럼이 없으면 0으로 채움(안정성)
            df[c] = 0
    
    # 날짜 정리: 대부분 20251001 형태일 것 -> datetime으로 변환
    df["date_raw"] = df["date_raw"].astype(str).str.strip()
    # 가능하다면 YYYYMMDD 형식 파싱
    def parse_date(s):
        s = s.strip()
        # 일부 행은 '20251001' 혹은 '2025-10-01' 등 다양한 형태일 수 있음
        for fmt in ("%Y%m%d", "%Y-%m-%d", "%Y.%m.%d"):
            try:
                return datetime.strptime(s, fmt).date()
            except:
                continue
        # 마지막으로 숫자만 골라 시도
        digits = "".join(ch for ch in s if ch.isdigit())
        if len(digits) == 8:
            return datetime.strptime(digits, "%Y%m%d").date()
        # 실패시 NaT
        return pd.NaT

    df["date"] = df["date_raw"].apply(parse_date)
    # drop rows without date
    df = df[~df["date"].isna()].copy()
    
    # station, line 컬럼이 없는 경우 기본 처리
    if "station" not in df.columns:
        # try second column name
        if len(df.columns) >= 2:
            df = df.rename(columns={df.columns[1]: "line"})
    if "line" not in df.columns:
        df["line"] = df.get("노선명", df.columns[1] if len(df.columns) > 1 else "알수없음")
    
    df["station"] = df["station"].astype(str).str.strip()
    df["line"] = df["line"].astype(str).str.strip()
    # 합계 칼럼
    df["total"] = df["in_cnt"] + df["out_cnt"]
    return df

# --- 경로: (앱에 업로드하거나 GitHub에 같이 올리세요) ---
DATA_PATH = "CARD_SUBWAY_MONTH_202510.csv"  # 같은 디렉토리에 파일을 올려두세요.

df = load_data(DATA_PATH)

# 필터: 2025-10에 해당하는 날짜들만 추출
df_oct2025 = df[df["date"].apply(lambda d: (d.year == 2025 and d.month == 10))]

if df_oct2025.empty:
    st.warning("데이터에 2025년 10월 기록이 없습니다. CSV 파일과 경로를 확인하세요.")
    st.stop()

# 사용자 입력 UI
unique_dates = sorted(df_oct2025["date"].dropna().unique())
date_choice = st.selectbox("📅 날짜 (2025년 10월)", unique_dates, format_func=lambda d: d.strftime("%Y-%m-%d"))

unique_lines = ["전체"] + sorted(df_oct2025["line"].dropna().unique())
line_choice = st.selectbox("🚉 호선 선택", unique_lines)

# 필터링
mask = (df_oct2025["date"] == date_choice)
if line_choice != "전체":
    mask &= (df_oct2025["line"] == line_choice)

df_filtered = df_oct2025[mask].copy()

if df_filtered.empty:
    st.info("선택한 날짜와 호선에 해당하는 데이터가 없습니다.")
    st.stop()

# 역별 합계 집계 및 상위 10개
top10 = (df_filtered.groupby(["station", "line"], as_index=False)
         .agg({"in_cnt":"sum","out_cnt":"sum","total":"sum"})
         .sort_values("total", ascending=False)
         .head(10)
         .reset_index(drop=True))

# 그래프: 1등 빨강, 나머지 파란 그라데이션
stations = top10["station"].tolist()
values = top10["total"].tolist()

def make_colors(n):
    # 첫 색: 선명한 빨강
    if n == 0:
        return []
    colors = []
    if n >= 1:
        colors.append("rgba(220,20,60,1.0)")  # crimson-ish red for 1등
    if n > 1:
        # blue base rgba(31,119,180) (plotly default blue)
        # alpha from 1.0 down to 0.35 for gradient
        alphas = np.linspace(1.0, 0.35, n-1)
        for a in alphas:
            colors.append(f"rgba(31,119,180,{a:.3f})")
    return colors

colors = make_colors(len(values))

fig = go.Figure(go.Bar(
    x=values[::-1],  # 역순으로 뒤집어서 막대가 큰값 위에 오게 (원하면 바꿀 수 있음)
    y=stations[::-1],
    orientation='h',
    marker=dict(color=colors[::-1]),  # 역순 보정
    hovertemplate="<b>%{y}</b><br>승차+하차: %{x:,}<extra></extra>"
))

fig.update_layout(
    title=f"{date_choice.strftime('%Y-%m-%d')} — {line_choice} (상위 10개 역)",
    xaxis_title="승차 + 하차 (명)",
    yaxis_title="역명",
    margin=dict(l=150, r=30, t=80, b=40),
    template="simple_white",
    height=600,
)

st.plotly_chart(fig, use_container_width=True)

# 하단: 표 보기
with st.expander("🔎 상위 10개 역 표 보기"):
    st.dataframe(top10[["station","line","in_cnt","out_cnt","total"]].rename(
        columns={"station":"역명","line":"호선","in_cnt":"승차","out_cnt":"하차","total":"합계"}
    ))

st.markdown("---")
st.caption("파일: `CARD_SUBWAY_MONTH_202510.csv` 을 앱과 같은 폴더에 업로드하거나, Streamlit Cloud에 배포할 때는 GitHub에 함께 올려주세요.")

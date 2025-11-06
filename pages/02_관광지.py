# app.py
import streamlit as st
from streamlit_folium import st_folium
import folium
from folium import Popup, IFrame

st.set_page_config(page_title="Seoul Top 10 (for foreign visitors)", layout="wide")

st.title("🌏 Seoul Top 10 — map (Folium + Streamlit)")
st.caption("외국인들이 좋아하는 서울 주요 관광지 Top10을 지도에 표시합니다.")

# 기본 서울 중심 좌표
SEOUL_CENTER = (37.5665, 126.9780)

# 장소 리스트: name, (lat, lon), short description, url (optional)
PLACES = [
    {
        "name": "Gyeongbokgung Palace (경복궁)",
        "coords": (37.579884, 126.9768),
        "desc": "조선시대의 대표 궁궐 — 경복궁.",
        "url": "https://en.wikipedia.org/wiki/Gyeongbokgung"
    },
    {
        "name": "Changdeokgung Palace (창덕궁)",
        "coords": (37.582108, 126.991663),
        "desc": "유네스코 세계문화유산으로 알려진 궁궐.",
        "url": "https://en.wikipedia.org/wiki/Changdeokgung"
    },
    {
        "name": "Bukchon Hanok Village (북촌한옥마을)",
        "coords": (37.58218, 126.98326),
        "desc": "전통 한옥이 모여 있는 고즈넉한 마을.",
        "url": "https://en.wikipedia.org/wiki/Bukchon_Hanok_Village"
    },
    {
        "name": "N Seoul Tower (남산서울타워)",
        "coords": (37.551170, 126.988228),
        "desc": "서울을 한눈에 보는 전망 타워.",
        "url": "https://en.wikipedia.org/wiki/N_Seoul_Tower"
    },
    {
        "name": "Myeongdong (명동)",
        "coords": (37.564, 126.985),
        "desc": "쇼핑과 스트리트푸드로 유명한 번화가.",
        "url": "https://en.wikipedia.org/wiki/Myeongdong"
    },
    {
        "name": "Hongdae (홍대)",
        "coords": (37.55528, 126.92333),
        "desc": "젊음과 예술, 밤문화를 즐기기 좋은 지역.",
        "url": "https://en.wikipedia.org/wiki/Hongdae_(area)"
    },
    {
        "name": "Insadong (인사동)",
        "coords": (37.574165, 126.98491),
        "desc": "전통 공예와 찻집, 기념품 상점이 많은 거리.",
        "url": "https://en.wikipedia.org/wiki/Insadong"
    },
    {
        "name": "Dongdaemun Design Plaza (DDP, 동대문디자인플라자)",
        "coords": (37.5663, 127.0090),
        "desc": "현대적 건축과 전시가 열리는 디자인 랜드마크.",
        "url": "https://en.wikipedia.org/wiki/Dongdaemun_Design_Plaza"
    },
    {
        "name": "Namdaemun Market (남대문시장)",
        "coords": (37.5557, 126.9731),
        "desc": "전통 시장 — 쇼핑과 길거리 음식의 성지.",
        "url": "https://en.wikipedia.org/wiki/Namdaemun_Market"
    },
    {
        "name": "Yeouido Hangang Park (여의도 한강공원)",
        "coords": (37.52389, 126.92667),
        "desc": "한강변에서 산책, 자전거, 피크닉을 즐길 수 있는 공원.",
        "url": "https://en.wikipedia.org/wiki/Yeouido"
    },
]

# 사이드바: 장소 선택
st.sidebar.header("Controls")
place_names = [p["name"] for p in PLACES]
selected = st.sidebar.selectbox("Zoom to...", ["Seoul center"] + place_names)

# 지도 생성
m = folium.Map(location=SEOUL_CENTER, zoom_start=12, tiles="CartoDB positron")

# 마커 추가
for p in PLACES:
    name = p["name"]
    lat, lon = p["coords"]
    desc = p["desc"]
    url = p.get("url", "")
    # Popup content as small HTML
    html = f"<h4>{name}</h4><p>{desc}</p>"
    if url:
        html += f'<p><a href="{url}" target="_blank">More info</a></p>'
    iframe = IFrame(html, width=220, height=140)
    popup = Popup(iframe, max_width=265)
    folium.Marker(
        location=(lat, lon),
        popup=popup,
        tooltip=name,
        icon=folium.Icon(icon="info-sign")
    ).add_to(m)

# 선택한 항목으로 지도를 중앙/확대
if selected != "Seoul center":
    # find coords
    for p in PLACES:
        if p["name"] == selected:
            m.location = p["coords"]
            m.zoom_start = 16
            # add a circle highlight
            folium.CircleMarker(location=p["coords"], radius=60, color="#3388ff", fill=False, weight=2, opacity=0.6).add_to(m)
            break

# 지도 렌더링 (streamlit_folium 사용)
st.subheader("Interactive map")
st.write("마커를 클릭하면 간단한 설명과 더보기 링크가 나와요.")
st_data = st_folium(m, width=1100, height=700)

# 하단: 리스트와 출처
st.subheader("Places (list)")
for p in PLACES:
    st.markdown(f"**{p['name']}** — {p['desc']}  \n(좌표: {p['coords'][0]:.6f}, {p['coords'][1]:.6f})  \n[자세히 보기]({p['url']})")

st.caption("데이터 출처: 여행 가이드·위키백과·관광 포탈 자료 등을 종합했어요.")

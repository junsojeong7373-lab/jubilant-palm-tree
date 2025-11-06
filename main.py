# app.py
import streamlit as st
from streamlit_folium import st_folium
import folium
from folium import Popup, IFrame

st.set_page_config(page_title="Seoul Top 10 (for foreign visitors)", layout="wide")

st.title("🌏 Seoul Top 10 — map (Folium + Streamlit)")
st.caption("외국인들이 좋아하는 서울 주요 관광지 Top10을 지도에 표시합니다.")

SEOUL_CENTER = (37.5665, 126.9780)

PLACES = [
    {"name": "Gyeongbokgung Palace (경복궁)", "coords": (37.579884, 126.9768), "desc": "조선시대의 대표 궁궐 — 경복궁.", "url": "https://en.wikipedia.org/wiki/Gyeongbokgung"},
    {"name": "Changdeokgung Palace (창덕궁)", "coords": (37.582108, 126.991663), "desc": "유네스코 세계문화유산으로 알려진 궁궐.", "url": "https://en.wikipedia.org/wiki/Changdeokgung"},
    {"name": "Bukchon Hanok Village (북촌한옥마을)", "coords": (37.58218, 126.98326), "desc": "전통 한옥이 모여 있는 고즈넉한 마을.", "url": "https://en.wikipedia.org/wiki/Bukchon_Hanok_Village"},
    {"name": "N Seoul Tower (남산서울타워)", "coords": (37.551170, 126.988228), "desc": "서울을 한눈에 보는 전망 타워.", "url": "https://en.wikipedia.org/wiki/N_Seoul_Tower"},
    {"name": "Myeongdong (명동)", "coords": (37.564, 126.985), "desc": "쇼핑과 스트리트푸드로 유명한 번화가.", "url": "https://en.wikipedia.org/wiki/Myeongdong"},
    {"name": "Hongdae (홍대)", "coords": (37.55528, 126.92333), "desc": "젊음과 예술, 밤문화를 즐기기 좋은 지역.", "url": "https://en.wikipedia.org/wiki/Hongdae_(area)"},
    {"name": "Insadong (인사동)", "coords": (37.574165, 126.98491), "desc": "전통 공예와 찻집, 기념품 상점이 많은 거리.", "url": "https://en.wikipedia.org/wiki/Insadong"},
    {"name": "Dongdaemun Design Plaza (DDP, 동대문디자인플라자)",

===== app.py =====

Streamlit + Folium app: Top 15 world tourist destinations with selection details

Save this file as app.py and deploy on Streamlit Cloud (or run locally with streamlit run app.py).

import streamlit as st from streamlit_folium import st_folium import folium

st.set_page_config(page_title="Top15 Tourist Map", layout="wide") st.title("🌍 Top 15 World Tourist Destinations — Interactive Map")

Top 15 list: name, coordinates, country, famous landmark, recommended food

DESTINATIONS = [ {"name": "Eiffel Tower, Paris", "lat": 48.8584, "lon": 2.2945, "country": "France", "landmark": "Eiffel Tower", "food": "Croissants / Baguette"}, {"name": "Colosseum, Rome", "lat": 41.8902, "lon": 12.4922, "country": "Italy", "landmark": "Colosseum", "food": "Pizza / Pasta"}, {"name": "Statue of Liberty, New York", "lat": 40.6892, "lon": -74.0445, "country": "USA", "landmark": "Statue of Liberty", "food": "New York-style Pizza / Bagels"}, {"name": "Great Wall (Badaling), Beijing", "lat": 40.3542, "lon": 116.0200, "country": "China", "landmark": "Great Wall (Badaling)", "food": "Peking duck / Jiaozi (dumplings)"}, {"name": "Machu Picchu", "lat": -13.1631, "lon": -72.5450, "country": "Peru", "landmark": "Machu Picchu citadel", "food": "Ceviche / Lomo Saltado"}, {"name": "Taj Mahal, Agra", "lat": 27.1751, "lon": 78.0421, "country": "India", "landmark": "Taj Mahal", "food": "Biryani / Butter Chicken"}, {"name": "Pyramids of Giza", "lat": 29.9792, "lon": 31.1342, "country": "Egypt", "landmark": "Great Pyramid of Giza", "food": "Koshari / Falafel"}, {"name": "Grand Canyon (South Rim)", "lat": 36.0544, "lon": -112.1401, "country": "USA", "landmark": "Grand Canyon South Rim", "food": "Barbecue / Southwestern cuisine"}, {"name": "Sydney Opera House", "lat": -33.8568, "lon": 151.2153, "country": "Australia", "landmark": "Sydney Opera House", "food": "Fish and chips / Australian lamb"}, {"name": "Christ the Redeemer, Rio", "lat": -22.9519, "lon": -43.2105, "country": "Brazil", "landmark": "Christ the Redeemer", "food": "Feijoada / Acarajé"}, {"name": "Angkor Wat", "lat": 13.4125, "lon": 103.8667, "country": "Cambodia", "landmark": "Angkor Wat temple complex", "food": "Fish amok / Lok lak"}, {"name": "Mount Fuji", "lat": 35.3606, "lon": 138.7274, "country": "Japan", "landmark": "Mount Fuji", "food": "Sushi / Ramen"}, {"name": "Oia, Santorini", "lat": 36.4615, "lon": 25.3758, "country": "Greece", "landmark": "Blue-domed churches of Oia", "food": "Moussaka / Souvlaki"}, {"name": "Lake Louise (Banff)", "lat": 51.4160, "lon": -116.2120, "country": "Canada", "landmark": "Lake Louise", "food": "Poutine / Canadian maple treats"}, {"name": "Burj Khalifa, Dubai", "lat": 25.1972, "lon": 55.2744, "country": "UAE", "landmark": "Burj Khalifa", "food": "Shawarma / Middle Eastern mezze"}, ]

Sidebar controls

st.sidebar.header("지도 설정") show_all = st.sidebar.checkbox("모든 관광지 마커 보기", value=True) initial_zoom = st.sidebar.slider("초기 줌 레벨", min_value=1, max_value=12, value=2)

Selection box for the 15 destinations

names = [d["name"] for d in DESTINATIONS] selected = st.selectbox("15개 관광지 중에서 선택하세요:", ["-- 선택 없음 --"] + names)

Create Folium map (centered globally or centered on selection)

if selected and selected != "-- 선택 없음 --": sel = next(d for d in DESTINATIONS if d["name"] == selected) center = (sel["lat"], sel["lon"]) zoom_start = 6 else: center = (20, 0)  # global center zoom_start = initial_zoom

m = folium.Map(location=center, zoom_start=zoom_start, tiles="OpenStreetMap")

Add markers

for d in DESTINATIONS: popup_html = f"<b>{d['name']}</b><br><i>{d['country']}</i><br>Famous: {d['landmark']}<br>Recommended food: {d['food']}" folium.Marker(location=(d['lat'], d['lon']), popup=popup_html, tooltip=d['name']).add_to(m)

If user selected one, add a highlighted circle marker and show details panel

if selected and selected != "-- 선택 없음 --": folium.CircleMarker(location=(sel['lat'], sel['lon']), radius=12, color='red', fill=True, fill_opacity=0.7).add_to(m) st.markdown("### 선택한 관광지 정보") st.write(f"이름: {sel['name']}") st.write(f"나라: {sel['country']}") st.write(f"가장 유명한 명소/랜드마크: {sel['landmark']}") st.write(f"추천 음식: {sel['food']}")

# Small photo suggestion area (users can add images themselves)
st.info("팁: 더 풍부한 정보를 원하면 이미지를 업로드하거나 위키피디아/여행 사이트 링크를 추가하세요.")

Layout: map on the left, list on the right

col1, col2 = st.columns((2, 1)) with col1: st.subheader("세계 지도") st_folium(m, width="100%", height=650)

with col2: st.subheader("관광지 요약 (Top 15)") for idx, d in enumerate(DESTINATIONS, start=1): st.markdown(f"{idx}. {d['name']}") st.write(f"- 랜드마크: {d['landmark']}") st.write(f"- 추천 음식: {d['food']}") st.write("---")

st.caption("이 앱은 예시용이며, 더 많은 정보(사진, 링크, 상세 설명)를 추가해 확장할 수 있습니다.")

===== requirements.txt =====

Save the following content into a separate file named requirements.txt when deploying to Streamlit Cloud.

requirements.txt content:

streamlit==1.26.0

folium==0.14.0

streamlit-folium==0.12.0

(Streamlit Cloud will automatically install packages listed in requirements.txt)

===== Quick deploy notes =====

1. Create a GitHub repo with two files: app.py (this file) and requirements.txt (with the three packages above).

2. On Streamlit Cloud, "New app" -> connect your GitHub repo -> pick the branch and app.py -> deploy.

3. If you see map tiles not loading on first deploy, check that streamlit-folium is installed and that Folium can access tile servers.

4. To add images or external links for each destination, extend the DESTINATIONS list with 'image' or 'link' keys.

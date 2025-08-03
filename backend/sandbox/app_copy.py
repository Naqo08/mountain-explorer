# import streamlit as st
# import requests

# # API_BASE = "http://localhost:8000/api"
# BACKEND_URL = "http://127.0.0.1:8000"

# st.set_page_config(page_title="Mountain Explorer", layout="wide")

# # --- Title / Hero Section ---
# st.markdown("""
# <style>
# .hero {
#     text-align: center;
#     margin-bottom: 2rem;
# }
# .hero h1 {
#     font-size: 3rem;
#     margin-bottom: 0.5rem;
# }
# .hero p {
#     font-size: 1.2rem;
#     color: gray;
# }
# </style>
# <div class="hero">
#     <h1>🏔️ Discover Famous Mountains Around the World</h1>
#     <p>Explore majestic peaks, learn fascinating facts, and plan your next mountain adventure with our comprehensive mountain database.</p>
# </div>
            
# """, unsafe_allow_html=True)

# # --- Fetch data ---
# @st.cache_data
# def fetch_mountains():
#   res = requests.get(f"{BACKEND_URL}/api/mountains")
#   return res.json() if res.status_code == 200 else []

# mountains = fetch_mountains()

# # --- Extract filters ---
# continents = sorted(set(m["continent"] for m in mountains))
# countries = sorted(set(m["location"] for m in mountains))

# col1, col2 = st.columns([1, 1])
# with col1:
#   selected_continent = st.selectbox("🌍 Filter by Continent", ["All"] + continents)
# with col2:
#   selected_country = st.selectbox("📍 Filter by Country", ["All"] + countries)

# # --- Filter logic ---
# def filter_mountain(m):
#   if selected_continent != "All" and m["continent"] != selected_continent:
#       return False
#   if selected_country != "All" and m["location"] != selected_country:
#       return False
#   return True

# filtered = list(filter(filter_mountain, mountains))

# # --- Display Grid Cards ---
# st.markdown("## 🏕️ Mountains")
# cols = st.columns(3)

# for idx, mountain in enumerate(filtered):
#   with cols[idx % 3]:
#     image_url = f"{BACKEND_URL}{mountain['image']}"
#     st.image(image_url, use_container_width=True, caption=mountain["name"])
#     st.markdown(f"### {mountain['name']}")
#     st.markdown(f"🗻 **{mountain['height']:,} m**")
#     st.markdown(f"📍 {mountain['location']}")

#     if st.button(f"🔍 AI Fact: {mountain['name']}", key=f"ai_{mountain['id']}"):
#       with st.spinner("Thinking..."):
#         ai_res = requests.get(f"{BACKEND_URL}/api/mountains/{mountain['id']}/ai-facts")
#         if "facts" in ai_res.json():
#             st.success(ai_res.json()["facts"])
#         else:
#               st.error("No AI facts available.")

# st.markdown("---")
# st.caption("© 2024 Mountain Explorer. All rights reserved.")

import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Mountain Explorer", layout="wide")

# --- Title / Hero Section ---
st.markdown("""
<style>
.hero {
    text-align: center;
    margin-bottom: 2rem;
}
.hero h1 {
    font-size: 3rem;
    margin-bottom: 0.5rem;
}
.hero p {
    font-size: 1.2rem;
    color: gray;
}
</style>
<div class="hero">
    <h1>🏔️ Discover Famous Mountains Around the World</h1>
    <p>Explore majestic peaks, learn fascinating facts, and plan your next mountain adventure with our comprehensive mountain database.</p>
</div>
""", unsafe_allow_html=True)

# --- Fetch data ---
@st.cache_data
def fetch_mountains():
    try:
        res = requests.get(f"{BACKEND_URL}/api/mountains")
        if res.status_code == 200:
            return res.json()
        else:
            st.error(f"Failed to fetch mountains: {res.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        st.error(f"Connection error: {e}")
        return []

mountains = fetch_mountains()

if not mountains:
    st.error("No mountains data available. Please check if the backend is running.")
    st.stop()

# --- Extract filters ---
continents = sorted(set(m["continent"] for m in mountains))
countries = sorted(set(m["location"] for m in mountains))

col1, col2 = st.columns([1, 1])
with col1:
    selected_continent = st.selectbox("🌍 Filter by Continent", ["All"] + continents)
with col2:
    selected_country = st.selectbox("📍 Filter by Country", ["All"] + countries)

# --- Filter logic ---
def filter_mountain(m):
    if selected_continent != "All" and m["continent"] != selected_continent:
        return False
    if selected_country != "All" and m["location"] != selected_country:
        return False
    return True

filtered = list(filter(filter_mountain, mountains))

# --- Display Grid Cards ---
st.markdown("## 🏕️ Mountains")
cols = st.columns(3)

for idx, mountain in enumerate(filtered):
    with cols[idx % 3]:
        image_url = f"{BACKEND_URL}{mountain['image']}"
        
        # Try to display image with error handling
        try:
            st.image(image_url, use_container_width=True, caption=mountain["name"])
        except Exception as e:
            st.error(f"Could not load image for {mountain['name']}")
        
        st.markdown(f"### {mountain['name']}")
        st.markdown(f"🗻 **{mountain['height']:,} m**")
        st.markdown(f"📍 {mountain['location']}")
        st.markdown(f"🏔️ {mountain['range']}")
        st.markdown(f"📅 First ascent: {mountain['first_ascent']}")

        if st.button(f"🔍 AI Fact: {mountain['name']}", key=f"ai_{mountain['id']}"):
            with st.spinner("Thinking..."):
                try:
                    ai_res = requests.get(f"{BACKEND_URL}/api/mountains/{mountain['id']}/ai-facts")
                    if ai_res.status_code == 200 and "facts" in ai_res.json():
                        st.success(ai_res.json()["facts"])
                    else:
                        st.error("No AI facts available.")
                except Exception as e:
                    st.error(f"Error fetching AI facts: {e}")

st.markdown("---")
st.caption("© 2024 Mountain Explorer. All rights reserved.")

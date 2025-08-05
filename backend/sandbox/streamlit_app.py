# import streamlit as st
# import requests

# BACKEND_URL = "http://127.0.0.1:8000"

# st.set_page_config(page_title="Mountain Explorer", layout="wide")

# # --- CSS for consistent card heights ---
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

# div[data-testid="column"] {
#     height: 100%;
# }

# .mountain-card {
#     border: 1px solid #ddd;
#     border-radius: 10px;
#     padding: 1rem;
#     background-color: #f9f9f9;
#     height: 500px;
#     display: flex;
#     flex-direction: column;
# }

# .mountain-content {
#     flex-grow: 1;
#     display: flex;
#     flex-direction: column;
#     justify-content: space-between;
# }
# </style>
# """, unsafe_allow_html=True)

# # --- Title / Hero Section ---
# st.markdown("""
# <div class="hero">
#     <h1>🏔️ Discover Famous Mountains Around the World</h1>
#     <p>Explore majestic peaks, learn fascinating facts, and plan your next mountain adventure with our comprehensive mountain database.</p>
# </div>
# """, unsafe_allow_html=True)

# # --- Fetch data ---
# @st.cache_data
# def fetch_mountains():
#     try:
#         res = requests.get(f"{BACKEND_URL}/api/mountains")
#         if res.status_code == 200:
#             return res.json()
#         else:
#             st.error(f"Failed to fetch mountains: {res.status_code}")
#             return []
#     except requests.exceptions.RequestException as e:
#         st.error(f"Connection error: {e}")
#         return []

# mountains = fetch_mountains()

# if not mountains:
#     st.error("No mountains data available. Please check if the backend is running.")
#     st.stop()

# # --- Extract filters ---
# continents = sorted(set(m["continent"] for m in mountains))
# countries = sorted(set(m["location"] for m in mountains))

# col1, col2 = st.columns([1, 1])
# with col1:
#     selected_continent = st.selectbox("🌍 Filter by Continent", ["All"] + continents)
# with col2:
#     selected_country = st.selectbox("📍 Filter by Country", ["All"] + countries)

# # --- Filter logic ---
# def filter_mountain(m):
#     if selected_continent != "All" and m["continent"] != selected_continent:
#         return False
#     if selected_country != "All" and m["location"] != selected_country:
#         return False
#     return True

# filtered = list(filter(filter_mountain, mountains))

# # --- Display Grid Cards ---
# st.markdown("## 🏕️ Mountains")

# # Create rows of 3 columns each
# for i in range(0, len(filtered), 3):
#     cols = st.columns(3, gap="medium")
    
#     # Get up to 3 mountains for this row
#     row_mountains = filtered[i:i+3]
    
#     for col_idx, mountain in enumerate(row_mountains):
#         with cols[col_idx]:
#             with st.container():
#                 # Image with aspect ratio control
#                 image_url = f"{BACKEND_URL}{mountain['image']}"
#                 try:
#                     st.image(image_url, use_container_width=True)
#                 except Exception as e:
#                     st.error(f"Could not load image")
                
#                 # Title
#                 st.markdown(f"### {mountain['name']}")
                
#                 # Details in a structured way
#                 st.write(f"🗻 **{mountain['height']:,} m**")
#                 st.write(f"📍 {mountain['location']}")
#                 st.write(f"🏔️ {mountain['range']}")
#                 st.write(f"📅 First ascent: {mountain['first_ascent']}")
                
#                 # Spacer to push button to bottom
#                 st.write("")
                
#                 # AI Facts button
#                 if st.button(f"🔍 AI Facts", key=f"ai_{mountain['id']}", use_container_width=True):
#                     with st.spinner("Generating facts..."):
#                         try:
#                             ai_res = requests.get(f"{BACKEND_URL}/api/mountains/{mountain['id']}/ai-facts")
#                             if ai_res.status_code == 200 and "facts" in ai_res.json():
#                                 st.success(ai_res.json()["facts"])
#                             else:
#                                 st.error("No AI facts available.")
#                         except Exception as e:
#                             st.error(f"Error: {e}")

# # Handle case where there are no filtered results
# if not filtered:
#     st.info("No mountains match your current filters. Try adjusting your selection.")

# st.markdown("---")
# st.caption("© 2024 Mountain Explorer. All rights reserved.")

import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Mountain Explorer", layout="wide")

# --- CSS for consistent card heights and image sizes ---
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

div[data-testid="column"] {
  height: 100%;
}

.mountain-card {
  border: 1px solid #ddd;
  border-radius: 10px;
  padding: 1rem;
  background-color: #f9f9f9;
  height: 500px;
  display: flex;
  flex-direction: column;
}

.mountain-content {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

/* Fixed image size styling */
.mountain-image {
  width: 100% !important;
  height: 200px !important;
  object-fit: cover !important;
  border-radius: 8px !important;
  margin-bottom: 1rem !important;
}

/* Override Streamlit's default image styling */
.stImage > img {
  width: 100% !important;
  height: 200px !important;
  object-fit: cover !important;
  border-radius: 8px !important;
}

div[data-testid="stImage"] {
  height: 200px !important;
}

div[data-testid="stImage"] > img {
  height: 200px !important;
  object-fit: cover !important;
}
</style>
""", unsafe_allow_html=True)

# --- Title / Hero Section ---
st.markdown("""
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

# Create rows of 3 columns each
for i in range(0, len(filtered), 3):
  cols = st.columns(3, gap="medium")
    
  # Get up to 3 mountains for this row
  row_mountains = filtered[i:i+3]
  
  for col_idx, mountain in enumerate(row_mountains):
    with cols[col_idx]:
      with st.container():
          # Image with fixed dimensions
          image_url = f"{BACKEND_URL}{mountain['image']}"
          try:
            # Using a container div to ensure consistent sizing
            st.markdown(f"""
            <div style="height: 200px; width: 100%; overflow: hidden; border-radius: 8px; margin-bottom: 1rem;">
                <img src="{image_url}" style="width: 100%; height: 100%; object-fit: cover;" alt="{mountain['name']}">
            </div>
            """, unsafe_allow_html=True)
          except Exception as e:
            # Fallback placeholder for missing images
            st.markdown(f"""
            <div style="height: 200px; width: 100%; background-color: #e0e0e0; border-radius: 8px; margin-bottom: 1rem; display: flex; align-items: center; justify-content: center; color: #666;">
                <span>Image not available</span>
            </div>
            """, unsafe_allow_html=True)
          
          # Title
          st.markdown(f"### {mountain['name']}")
          
          # Details in a structured way
          st.write(f"🗻 **{mountain['height']:,} m**")
          st.write(f"📍 {mountain['location']}")
          st.write(f"🏔️ {mountain['range']}")
          st.write(f"📅 First ascent: {mountain['first_ascent']}")
          
          # Spacer to push button to bottom
          st.write("")
          
          # AI Facts button
          if st.button(f"🔍 AI Facts", key=f"ai_{mountain['id']}", use_container_width=True):
            with st.spinner("Generating facts..."):
              try:
                ai_res = requests.get(f"{BACKEND_URL}/api/mountains/{mountain['id']}/ai-facts")
                if ai_res.status_code == 200 and "facts" in ai_res.json():
                  st.success(ai_res.json()["facts"])
                else:
                  st.error("No AI facts available.")
              except Exception as e:
                  st.error(f"Error: {e}")

# Handle case where there are no filtered results
if not filtered:
  st.info("No mountains match your current filters. Try adjusting your selection.")

st.markdown("---")
st.caption("© 2024 Mountain Explorer. All rights reserved.")
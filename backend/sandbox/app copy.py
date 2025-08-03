import streamlit as st
import requests
import textwrap

# --- Configuration ---
BACKEND_URL = "http://127.0.0.1:8000" # URL of your FastAPI backend

# --- Page Configuration ---
st.set_page_config(
    page_title="Mountain Explorer",
    page_icon="🏔️",
    layout="wide", # Use "centered" or "wide"
)

# --- Custom CSS to mimic the React design ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# We will create a style.css file for cleaner code
# For now, let's inject CSS directly for simplicity.
st.markdown("""
<style>
    /* Main container styling */
    .stApp {
        background-color: #f8f9fa;
    }

    /* Header and Title */
    .header {
        background-color: #ffffff;
        padding: 1rem 2rem;
        border-bottom: 1px solid #dee2e6;
        margin-bottom: 2rem;
    }
    .header .logo {
        font-size: 2rem;
        font-weight: 700;
        color: #0d1b2a;
    }

    /* Card styling */
    .card {
        background-color: white;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        transition: transform 0.2s;
        padding: 1.5rem;
        display: flex;
        flex-direction: column;
        height: 100%;
    }
    .card:hover {
        transform: translateY(-5px);
    }
    .card img {
        border-radius: 8px;
        width: 100%;
        height: 200px;
        object-fit: cover;
        margin-bottom: 1rem;
    }
    .card-title {
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .card-text {
        color: #415a77;
        margin-bottom: 1rem;
    }
    
    /* Button styling */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #415a77;
        color: white;
        padding: 0.75rem;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #0d1b2a;
        color: white;
    }

    /* AI facts box */
    .ai-facts {
        background-color: #e0e1dd;
        border-radius: 8px;
        padding: 1rem;
        margin-top: 1rem;
        font-style: italic;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)


# --- API Communication ---
@st.cache_data(ttl=600) # Cache data for 10 minutes
def get_all_mountains():
    """Fetches all mountains from the backend."""
    try:
        response = requests.get(f"{BACKEND_URL}/api/mountains")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching mountains: {e}")
        return []

@st.cache_data(ttl=60) # Shorter cache for dynamic AI content
def get_ai_facts(mountain_id):
    """Fetches AI-generated facts for a specific mountain."""
    try:
        response = requests.get(f"{BACKEND_URL}/api/mountains/{mountain_id}/ai-facts")
        response.raise_for_status()
        return response.json().get("facts", "Could not retrieve AI facts.")
    except requests.exceptions.RequestException as e:
        return f"Error fetching AI facts: {e}"

# --- Main App Logic ---

# Initialize session state for navigation
if 'selected_mountain' not in st.session_state:
    st.session_state.selected_mountain = None

mountains = get_all_mountains()

# --- Header ---
st.markdown("""
    <div class="header">
        <div class="logo">🏔️ Mountain Explorer</div>
    </div>
""", unsafe_allow_html=True)


# --- Main Content Area ---
if st.session_state.selected_mountain:
    # --- DETAIL VIEW ---
    mountain = st.session_state.selected_mountain
    
    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.image(mountain['image'], caption=mountain['name'])

    with col2:
        st.title(mountain['name'])
        st.subheader(f"△ {mountain['height']} m | 📍 {mountain['location']}")
        st.markdown(f"**Continent:** {mountain['continent']}")
        st.markdown(f"**Range:** {mountain['range']}")
        st.markdown(f"**First Ascent:** {mountain['first_ascent']}")

        if st.button("✨ Generate AI Facts"):
            with st.spinner("🤖 Generating insights..."):
                ai_facts = get_ai_facts(mountain['id'])
                st.markdown(f"<div class='ai-facts'>{ai_facts}</div>", unsafe_allow_html=True)
                
    if st.button("← Back to All Mountains"):
        st.session_state.selected_mountain = None
        st.rerun() # Rerun the script to show the grid view

else:
    # --- GRID VIEW ---
    st.title("Discover Famous Mountains Around the World")
    st.markdown("Explore majestic peaks, learn fascinating facts, and plan your next mountain adventure.")

    # --- Filtering ---
    if mountains:
        continents = ["All"] + sorted(list(set(m['continent'] for m in mountains)))
        selected_continent = st.selectbox("Filter by Continent", continents)

        if selected_continent == "All":
            filtered_mountains = mountains
        else:
            filtered_mountains = [m for m in mountains if m['continent'] == selected_continent]

        # --- Display Mountain Grid ---
        cols = st.columns(3) # Create 3 columns
        for i, mountain in enumerate(filtered_mountains):
            with cols[i % 3]:
                # Create a "card" using markdown and HTML
                st.markdown(f"""
                <div class="card">
                    <img src="{mountain['image']}" alt="{mountain['name']}">
                    <div class="card-title">{mountain['name']}</div>
                    <div class="card-text">△ {mountain['height']} m</div>
                    <div class="card-text">📍 {mountain['location']}</div>
                </div>
                """, unsafe_allow_html=True)

                if st.button("View Details", key=f"details_{mountain['id']}"):
                    st.session_state.selected_mountain = mountain
                    st.rerun()
    else:
        st.warning("Could not load mountain data from the backend. Please ensure the backend server is running.")

# --- Footer ---
st.markdown("---")
st.markdown("© 2025 Mountain Explorer. Built with Streamlit and FastAPI.")
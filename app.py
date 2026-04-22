import streamlit as st

st.set_page_config(page_title="DPRES", page_icon="⛑️", layout="wide")

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

pages = {
    "Navigation": [
        st.Page("views/home.py", title="Basecamp", icon="📍"),
        st.Page("views/learning.py", title="Survival Guides", icon="🎒"),
        st.Page("views/mapping.py", title="Interactive Mapping", icon="🗺️"),
        st.Page("views/gobag.py", title="Go-Bag Builder", icon="🧳"),
        st.Page("views/directory.py", title="SOS Directory", icon="📇"),
        st.Page("views/quiz.py", title="Knowledge Assessment", icon="📝"),
        st.Page("views/dashboard.py", title="Readiness Metrics", icon="📋"),
    ]
}

pg = st.navigation(pages)

with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #FF4B4B; margin-bottom: 0;'>DPRES</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; opacity: 0.6; font-size: 0.8rem; margin-top: 0;'>Disaster Preparedness & Response</p>", unsafe_allow_html=True)
    st.markdown("---")
    st.caption("Protocol v4.2.0-Live")

pg.run()




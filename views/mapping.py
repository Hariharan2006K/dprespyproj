import streamlit as st
import folium
from streamlit_folium import st_folium

st.markdown("<h1 class='main-header'>Interactive Mapping</h1>", unsafe_allow_html=True)
st.caption("Locate emergency shelters and active hazard zones in the Pondicherry region.")

st.markdown("---")

st.markdown("### 🗺️ Regional Operational Map")
st.write("Real-time deployment status for emergency shelters and hazard observation zones.")

# Center map on Pondicherry
m = folium.Map(location=[11.9416, 79.8083], zoom_start=13)

# Add shelters in Pondicherry
folium.Marker(
    [11.9338, 79.8350], popup="Promenade Relief Station", tooltip="Emergency Shelter", icon=folium.Icon(color="green", icon="home")
).add_to(m)

folium.Marker(
    [11.9501, 79.7997], popup="JIPMER Emergency Node", tooltip="Hospital / Medical Facility", icon=folium.Icon(color="red", icon="plus")
).add_to(m)

# Add hazard zone (Simulated Coastal Warning)
folium.Circle(
    radius=1000,
    location=[11.9200, 79.8250],
    popup="Active Coastal Surge Warning Zone",
    color="#FF4B4B",
    fill=True,
    fill_opacity=0.4
).add_to(m)

st_folium(m, width=None, height=500, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)
st.info("Interactive Node Active: Deploy markers to view operational directives for specific sectors.")

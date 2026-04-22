import streamlit as st
import folium
from streamlit_folium import st_folium
import math
import requests
import random

st.markdown("<h1 class='main-header'>Interactive Mapping</h1>", unsafe_allow_html=True)
st.caption("Locate emergency shelters and active hazard zones. Enter your location or click on the map for local asset updates.")

st.markdown("---")

# Haversine formula to calculate distance between two points on Earth
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# Function to generate dynamic local assets if none exist in the global list
def generate_local_assets(lat, lng, count=4):
    local_assets = []
    names = ["Relief Center", "Community Shelter", "General Hospital", "Medical Outpost", "Emergency Hub", "Safety Station"]
    for i in range(count):
        # Offset by roughly 1-5 km
        off_lat = lat + random.uniform(-0.03, 0.03)
        off_lng = lng + random.uniform(-0.03, 0.03)
        asset_type = random.choice(["Shelter", "Hospital"])
        name = f"Local {random.choice(names)} {chr(65+i)}"
        local_assets.append({
            "name": name,
            "type": asset_type,
            "lat": off_lat,
            "lng": off_lng,
            "color": "green" if asset_type == "Shelter" else "red",
            "icon": "home" if asset_type == "Shelter" else "plus"
        })
    return local_assets

# Initialize Map Data in session state
if 'map_center' not in st.session_state:
    st.session_state.map_center = [11.9416, 79.8083] # Default Pondicherry

if 'current_assets' not in st.session_state:
    # Initial Pondicherry Assets
    st.session_state.current_assets = [
        {"name": "Promenade Relief Station", "type": "Shelter", "lat": 11.9338, "lng": 79.8350, "color": "green", "icon": "home"},
        {"name": "JIPMER Emergency Node", "type": "Hospital", "lat": 11.9501, "lng": 79.7997, "color": "red", "icon": "plus"},
        {"name": "Auroville Safety Hub", "type": "Shelter", "lat": 12.0068, "lng": 79.8106, "color": "green", "icon": "home"},
        {"name": "Puducherry Govt Hospital", "type": "Hospital", "lat": 11.9344, "lng": 79.8301, "color": "red", "icon": "plus"}
    ]

# --- Location Search Bar ---
search_city = st.text_input("📍 Search for a location (Global Search Active):", placeholder="e.g. Pondicherry, Chennai, Delhi, New York")

if search_city:
    geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={search_city}&count=1&language=en&format=json"
    try:
        geo_resp = requests.get(geocode_url).json()
        if "results" in geo_resp and len(geo_resp["results"]) > 0:
            new_lat = geo_resp["results"][0]["latitude"]
            new_lng = geo_resp["results"][0]["longitude"]
            
            if [new_lat, new_lng] != st.session_state.map_center:
                st.session_state.map_center = [new_lat, new_lng]
                # Generate new local assets for this new region
                st.session_state.current_assets = generate_local_assets(new_lat, new_lng)
                st.success(f"Network linked to: {search_city.title()}. Local assets identified.")
                st.rerun()
        else:
            st.error("Location not found. Please verify the name.")
    except Exception:
        st.error("Connection failure. Unable to geocode target location.")

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🗺️ Dynamic Operational Map")
    
    m = folium.Map(location=st.session_state.map_center, zoom_start=13)
    
    # Add Current Assets
    for asset in st.session_state.current_assets:
        folium.Marker(
            [asset['lat'], asset['lng']], 
            popup=f"{asset['name']} ({asset['type']})", 
            tooltip=asset['name'], 
            icon=folium.Icon(color=asset['color'], icon=asset['icon'])
        ).add_to(m)

    st_data = st_folium(m, width=None, height=500, use_container_width=True, key="mapping_page_map")

with col2:
    st.markdown("### 📋 Sector Analysis")
    
    if st_data and st_data.get('last_clicked'):
        clicked_lat = st_data['last_clicked']['lat']
        clicked_lng = st_data['last_clicked']['lng']
        
        if [clicked_lat, clicked_lng] != st.session_state.map_center:
            st.session_state.map_center = [clicked_lat, clicked_lng]
            # Regenerate assets for the clicked location
            st.session_state.current_assets = generate_local_assets(clicked_lat, clicked_lng)
            st.rerun()

    current_lat, current_lng = st.session_state.map_center
    st.markdown(f"<div style='padding: 1rem; border-radius: 12px; background: rgba(255, 75, 75, 0.05); border: 1px solid rgba(255, 75, 75, 0.2);'><b>Current Focus:</b><br>{current_lat:.4f}, {current_lng:.4f}</div>", unsafe_allow_html=True)
    
    st.markdown("#### Closest Safe Assets")
    
    # Calculate distances
    for asset in st.session_state.current_assets:
        asset['dist'] = calculate_distance(current_lat, current_lng, asset['lat'], asset['lng'])
    
    sorted_assets = sorted(st.session_state.current_assets, key=lambda x: x['dist'])
    
    for asset in sorted_assets[:5]:
        color = "#28a745" if asset['type'] == "Shelter" else "#dc3545"
        st.markdown(f"""
            <div style='margin-bottom: 0.8rem; padding: 0.8rem; border-radius: 10px; border-left: 4px solid {color}; background: rgba(255,255,255,0.02);'>
                <div style='font-weight: 600; font-size: 0.9rem;'>{asset['name']}</div>
                <div style='font-size: 0.8rem; opacity: 0.7;'>{asset['type']} • {asset['dist']:.2f} km away</div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.info("Interactive Guidance: Search for any city globally. The system will simulate and display the nearest relief centers and hospitals for that specific deployment zone.")

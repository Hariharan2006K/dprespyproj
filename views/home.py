import streamlit as st
import requests
import time

# Hero Section
st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(255, 75, 75, 0.1) 0%, rgba(0, 0, 0, 0) 100%); padding: 3rem; border-radius: 24px; border: 1px solid rgba(255, 75, 75, 0.2); margin-bottom: 2rem;'>
        <h1 class='main-header'>Welcome to Basecamp</h1>
        <p style='font-size: 1.2rem; opacity: 0.8;'>Strategic operational center for disaster education and response management. Access survival protocols, interactive mapping, and readiness metrics from this node.</p>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 🌡️ Weather Telemetry")
    st.write("Monitor real-time atmospheric conditions via the Open-Meteo framework.")
    
    city = st.text_input("Deploy sensor to city:", "New York", help="Enter city name to fetch live data")
    
    if city:
        geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
        try:
            geo_resp = requests.get(geocode_url).json()
            if "results" in geo_resp and len(geo_resp["results"]) > 0:
                lat = geo_resp["results"][0]["latitude"]
                lon = geo_resp["results"][0]["longitude"]
                
                weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
                weather_resp = requests.get(weather_url).json()
                
                if "current_weather" in weather_resp:
                    cw = weather_resp["current_weather"]
                    st.success(f"**Current conditions in {city.title()}:**\n\n{cw['temperature']}°C | Wind Speed: {cw['windspeed']} km/h")
            else:
                st.error(f"Target '{city}' unreachable. Verify coordinates.")
        except Exception as e:
            st.error("Telemetry link failure. Unable to retrieve environmental metrics.")

with col2:
    st.markdown("### 🚨 Alert Simulation")
    st.write("Execute a controlled drill of the regional broadcast system.")
    
    st.markdown("<div style='padding: 1rem; border-radius: 12px; background: rgba(255, 75, 75, 0.05); border-left: 4px solid #FF4B4B; margin-bottom: 1rem; font-size: 0.9rem; opacity: 0.8;'>Warning: Simulation triggers visual alerts across the node interface.</div>", unsafe_allow_html=True)
    
    if st.button("Initialize Drill Protocol", type="primary", use_container_width=True):
        st.toast("SYSTEM OVERRIDE: Emergency protocols activated.")
        time.sleep(0.5)
        st.warning("SIMULATION ACTIVE: This is a drill of the regional hazard alert system. No actual emergency detected.")

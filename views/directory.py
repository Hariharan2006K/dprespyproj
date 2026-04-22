import streamlit as st
import pandas as pd

st.markdown("<h1 class='main-header'>SOS Directory</h1>", unsafe_allow_html=True)
st.caption("Access critical emergency hotlines and operational support numbers.")

st.markdown("---")

region = st.selectbox("Operational Sector:", ["India (Pondicherry)", "North America", "Europe", "Global / Other"])

if region == "India (Pondicherry)":
    data = {
        "Service": ["General Emergency", "Police Control Room", "Fire & Rescue", "Ambulance", "Disaster Helpline", "Coastal Security"],
        "Number": ["112", "100 / 0413-2231400", "101 / 0413-2334321", "108 / 102", "1070 / 1077", "1093"]
    }
elif region == "North America":
    data = {"Service": ["General Emergency", "Poison Control", "FEMA Hotline", "Red Cross"], "Number": ["911", "1-800-222-1222", "1-800-621-3362", "1-800-RED-CROSS"]}
elif region == "Europe":
    data = {"Service": ["General Emergency", "Medical Advice", "Fire Brigade", "Police"], "Number": ["112", "111 (UK)", "112 / 18 (FR)", "112 / 17 (FR)"]}
else:
    data = {"Service": ["General Emergency (Aus)", "SES Flood/Storm (Aus)", "General Emergency (NZ)"], "Number": ["000", "132 500", "111"]}

df = pd.DataFrame(data)

st.markdown(f"### 📞 {region} Emergency Assets")
st.dataframe(df, use_container_width=True, hide_index=True)

st.markdown("<br>", unsafe_allow_html=True)
st.warning("Critical Protocol: Ensure your immediate safety before attempting to establish a telemetry link with emergency services.")

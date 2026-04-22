import streamlit as st

st.markdown("<h1 class='main-header'>Go-Bag Builder</h1>", unsafe_allow_html=True)
st.caption("Pack your digital survival kit and monitor your preparedness readiness score.")

st.markdown("---")

items = [
    "Water (1 gallon per person per day for 3 days)",
    "Non-perishable food (3-day supply)",
    "Battery-powered or hand-crank radio",
    "Flashlight with extra batteries",
    "First aid kit",
    "Whistle (to signal for help)",
    "Dust mask (to filter contaminated air)",
    "Moist towelettes and garbage bags (for personal sanitation)",
    "Wrench or pliers (to turn off utilities)",
    "Manual can opener",
    "Local maps",
    "Cell phone with chargers and backup battery"
]

st.markdown("### 🎒 Inventory Checklist")
st.write("Confirm the possession of critical survival assets for your 72-hour kit:")

col1, col2 = st.columns(2)

checked_items = []
for i, item in enumerate(items):
    # Split items between two columns
    target_col = col1 if i < len(items)/2 else col2
    with target_col:
        checked = st.checkbox(item, key=f"gobag_{i}")
        if checked:
            checked_items.append(item)

st.markdown("---")
st.markdown("### 📊 Readiness Status")
progress = len(checked_items) / len(items)

st.progress(progress)
st.markdown(f"<div style='text-align: center; font-size: 1.5rem; font-weight: 600; color: #FF4B4B;'>{int(progress*100)}% Complete</div>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; opacity: 0.6;'>{len(checked_items)} of {len(items)} critical items secured</p>", unsafe_allow_html=True)

if progress == 1.0:
    st.success("STATUS: FULLY PREPARED. Your Go-Bag is ready for immediate deployment.")
    st.balloons()
elif progress > 0.5:
    st.warning("STATUS: PARTIAL READINESS. Operational gaps identified in critical inventory.")
else:
    st.error("STATUS: INSUFFICIENT. Survival kit is below safe operational standards.")

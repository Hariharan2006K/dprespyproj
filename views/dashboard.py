import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.markdown("<h1 class='main-header'>Readiness Metrics</h1>", unsafe_allow_html=True)
st.caption("Review institutional engagement data and incident statistics powered by simulated protocol analytics.")

# Mock Data
total_users = 150
avg_score = 82.5
total_sims = 342
recent_scores = [
    ("Vishwa", 95, "2026-04-22 10:30"),
    ("Ganesh", 85, "2026-04-22 11:15"),
    ("Manvith", 99.5, "2026-04-22 12:45"),
    ("Hariharan", 100, "2026-04-22 13:20"),
    ("Symmalo Rao Sir", 90, "2026-04-22 14:05")
]

st.markdown("---")

# --- Key Metrics ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Personnel Evaluated", value=total_users, delta="+12% Since Last Cycle")
with col2:
    st.metric(label="Mean Assessment Score", value=f"{avg_score:.1f}/100", delta="+2.3")
with col3:
    st.metric(label="Simulations Conducted", value=total_sims, delta="+45")
with col4:
    st.metric(label="Active Regional Nodes", value=12, delta="Steady")

st.markdown("---")

# Row 1: Charts
r1c1, r1c2 = st.columns(2)

with r1c1:
    st.markdown("### 📊 Recent Evaluation Activity")
    df_scores = pd.DataFrame(recent_scores, columns=["Operator", "Score", "Timestamp"])
    st.dataframe(df_scores, use_container_width=True, hide_index=True)

with r1c2:
    st.markdown("### 🗺️ Regional Incident Distribution")
    pie_data = {
        "Hazard Type": ["Earthquakes", "Floods", "Fires", "Cyclones", "Heatwaves"],
        "Reported Instances": [15, 45, 20, 10, 30]
    }
    
    # Matplotlib Pie Chart
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    fig1.patch.set_facecolor('none')
    ax1.set_facecolor('none')
    
    colors = ['#FF4B4B', '#FF8F8F', '#FFCACA', '#D83131', '#9E1A1A']
    wedges, texts, autotexts = ax1.pie(
        pie_data["Reported Instances"], 
        labels=pie_data["Hazard Type"], 
        autopct='%1.1f%%', 
        startangle=140,
        colors=colors,
        textprops={'color':"w", 'fontsize': 10},
        pctdistance=0.85,
        explode=[0.05]*5
    )
    
    # Draw circle for donut effect
    centre_circle = plt.Circle((0,0),0.70,fc='#0E1117')
    fig1.gca().add_artist(centre_circle)
    
    ax1.axis('equal')  
    plt.tight_layout()
    st.pyplot(fig1)

st.markdown("---")

# Row 2: Line Chart
st.markdown("### 📈 Simulated Drill Attendance Trajectory")
line_data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Attendance (%)": [35, 38, 42, 40, 55, 60, 65, 70, 75, 78, 80, 82]
}

# Matplotlib Line Chart
fig2, ax2 = plt.subplots(figsize=(10, 4))
fig2.patch.set_facecolor('none')
ax2.set_facecolor('none')

ax2.plot(line_data["Month"], line_data["Attendance (%)"], marker='o', color='#FF4B4B', linewidth=3, markersize=8)

# Styling
ax2.set_ylabel('Participation Rate (%)', color='white', fontsize=10)
ax2.tick_params(axis='x', colors='white', labelsize=9)
ax2.tick_params(axis='y', colors='white', labelsize=9)
ax2.grid(True, linestyle='--', alpha=0.1, color='white')

# Remove top and right spines
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['bottom'].set_color('white')
ax2.spines['left'].set_color('white')

plt.tight_layout()
st.pyplot(fig2)

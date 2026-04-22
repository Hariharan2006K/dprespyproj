import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown("<h1 class='main-header'>Readiness Metrics</h1>", unsafe_allow_html=True)
st.caption("Review institutional engagement data and incident statistics powered by simulated protocol analytics.")

# Mock Data
total_users = 150
avg_score = 82.5
total_sims = 342
recent_scores = [
    ("Alice", 95, "2026-04-22 10:30"),
    ("Bob", 85, "2026-04-22 11:15"),
    ("Charlie", 70, "2026-04-22 12:45"),
    ("Diana", 100, "2026-04-22 13:20"),
    ("Eve", 90, "2026-04-22 14:05")
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

# Row 1: Interactive Charts
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
    df_pie = pd.DataFrame(pie_data)
    
    fig_pie = px.pie(
        df_pie, 
        names="Hazard Type", 
        values="Reported Instances", 
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig_pie.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )
    st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("---")

# Row 2: Line Chart
st.markdown("### 📈 Simulated Drill Attendance Trajectory")
line_data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Attendance (%)": [35, 38, 42, 40, 55, 60, 65, 70, 75, 78, 80, 82]
}
df_line = pd.DataFrame(line_data)

fig_line = px.line(
    df_line, 
    x="Month", 
    y="Attendance (%)", 
    markers=True,
    labels={"Attendance (%)": "Participation Rate (%)"}
)
fig_line.update_traces(line_color="#FF4B4B", line_width=3, marker_size=8)
fig_line.update_layout(
    margin=dict(l=20, r=20, t=40, b=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white'),
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
)
st.plotly_chart(fig_line, use_container_width=True)

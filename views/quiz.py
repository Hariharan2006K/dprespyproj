import streamlit as st
from fpdf import FPDF

st.markdown("<h1 class='main-header'>Knowledge Assessment</h1>", unsafe_allow_html=True)
st.caption("Perform a comprehensive evaluation of your understanding of hazard operational directives.")

# Function to generate PDF
def generate_pdf(name, score):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", style="B", size=24)
    pdf.cell(0, 20, "Certificate of Completion", new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.set_font("Helvetica", size=16)
    pdf.cell(0, 10, "This certifies that", new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.set_font("Helvetica", style="B", size=20)
    pdf.cell(0, 15, name, new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.set_font("Helvetica", size=16)
    pdf.cell(0, 10, "has successfully passed the DPRES Knowledge Assessment", new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.cell(0, 10, f"with a Readiness Score of {score} / 100.", new_x="LMARGIN", new_y="NEXT", align='C')
    return bytes(pdf.output())

# Initialize session state for safety score
if 'safety_score' not in st.session_state:
    st.session_state.safety_score = 0

if 'quiz_submitted' not in st.session_state:
    st.session_state.quiz_submitted = False

st.markdown("---")

# Ask for name for certificate
st.markdown("### 👤 Candidate Identification")
participant_name = st.text_input("Enter your full name for certification eligibility:", placeholder="e.g. John Doe")

questions = [
    {
        "q": "1. What is the immediate action you should take during an earthquake?",
        "options": ["Run outside", "Drop, Cover, and Hold On", "Stand in a doorway", "Get in an elevator"],
        "answer": "Drop, Cover, and Hold On"
    },
    {
        "q": "2. What should you do if you are driving when an earthquake starts?",
        "options": ["Speed up to outrun it", "Pull over to a clear location and stay in your car", "Park under a bridge", "Leave your car and run"],
        "answer": "Pull over to a clear location and stay in your car"
    },
    {
        "q": "3. After an earthquake, why should you turn off the main gas valve only if you suspect a leak?",
        "options": ["Because gas is too expensive", "Because only a professional can turn it back on", "Because it makes the house colder", "Because the valve might break"],
        "answer": "Because only a professional can turn it back on"
    },
    {
        "q": "4. What is the safest place to take cover during an earthquake?",
        "options": ["Next to a window", "Under a sturdy piece of furniture", "On the balcony", "Next to a tall bookshelf"],
        "answer": "Under a sturdy piece of furniture"
    },
    {
        "q": "5. What is the golden rule when encountering floodwaters?",
        "options": ["Swim through", "Turn Around, Don't Drown", "Drive slowly", "Measure the depth with a stick"],
        "answer": "Turn Around, Don't Drown"
    },
    {
        "q": "6. Why is it dangerous to walk through floodwaters?",
        "options": ["It can ruin your shoes", "As little as 6 inches of moving water can knock you down", "Water is too cold", "Fishes might bite"],
        "answer": "As little as 6 inches of moving water can knock you down"
    },
    {
        "q": "7. How should you prepare your home for a forecasted flood?",
        "options": ["Open all doors and windows", "Move essential items to upper floors", "Leave electronics plugged in", "Park your car in the basement"],
        "answer": "Move essential items to upper floors"
    },
    {
        "q": "8. What should you do if floodwaters reach your vehicle?",
        "options": ["Stay inside and roll up the windows", "Abandon it and move to higher ground if safe", "Try to push it out", "Reverse out quickly"],
        "answer": "Abandon it and move to higher ground if safe"
    },
    {
        "q": "9. How often should you test your smoke alarms?",
        "options": ["Once a week", "Once a month", "Once a year", "Never"],
        "answer": "Once a month"
    },
    {
        "q": "10. How should you move through a smoke-filled room?",
        "options": ["Run as fast as possible", "Walk upright holding your breath", "Crawl low under the smoke", "Wait for someone to rescue you"],
        "answer": "Crawl low under the smoke"
    }
]

st.markdown("---")
st.markdown("### 📝 Assessment Phase")

with st.form("quiz_form"):
    user_answers = []
    for i, q in enumerate(questions):
        st.markdown(f"<div style='padding: 1.5rem; border-radius: 12px; background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.05); margin-bottom: 1rem;'><b>{q['q']}</b></div>", unsafe_allow_html=True)
        ans = st.radio(f"Options for Q{i+1}", q['options'], key=f"q_{i}", label_visibility="collapsed")
        user_answers.append(ans)
        
    st.markdown("<br>", unsafe_allow_html=True)
    submitted = st.form_submit_button("Finalize Assessment")
    
    if submitted:
        if not participant_name:
            st.error("Identification required. Please enter your name at the top of the form.")
        else:
            score = 0
            st.session_state.quiz_submitted = True
            
            st.subheader("Evaluation Results")
            for i, q in enumerate(questions):
                if user_answers[i] == q['answer']:
                    score += 10
                else:
                    st.error(f"**Q{i+1}: Critical Error** - Selected: '{user_answers[i]}'. Operational Standard: '{q['answer']}'.")
                    
            st.session_state.safety_score = score

# Display Safety Score
if st.session_state.quiz_submitted:
    st.markdown("---")
    st.markdown(f"### Assessment Score: **{st.session_state.safety_score} / 100**")
    st.progress(st.session_state.safety_score / 100)
    
    if st.session_state.safety_score >= 80:
        st.info("Status: Operative Readiness Confirmed.")
        st.balloons()
        
        # Generator PDF
        pdf_bytes = generate_pdf(participant_name or "Participant", st.session_state.safety_score)
        st.download_button(
            label="Download Certification 🎓",
            data=pdf_bytes,
            file_name="DPRES_Certification.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    else:
        st.warning("Status: Remedial Training Required. Please review Survival Guides.")

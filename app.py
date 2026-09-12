import streamlit as st


# =====================================================
# PAGE SETTINGS
# =====================================================

st.set_page_config(
    page_title="SMARTMARK",
    page_icon="🎓",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #eef4ff, #f8f0ff);
}

.header {
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
}

.header h1 {
    font-size: 38px;
    margin: 0;
}

.header p {
    font-size: 17px;
    margin-top: 8px;
}

.card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.success-card {
    background: #ecfdf5;
    padding: 20px;
    border-radius: 15px;
    border-left: 6px solid #10b981;
}

.warning-card {
    background: #fff7ed;
    padding: 20px;
    border-radius: 15px;
    border-left: 6px solid #f97316;
}

.footer {
    text-align: center;
    color: #64748b;
    padding: 25px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# SESSION STATE
# =====================================================

if "page" not in st.session_state:
    st.session_state.page = "details"

if "student_data" not in st.session_state:
    st.session_state.student_data = None

# =====================================================
# SUBJECTS
# =====================================================

subjects = [
    "Discrete Mathematics",
    "Foundation of Data Science",
    "Data Structure & Algorithm",
    "DPCO",
    "Programming"
]

# =====================================================
# PAGE 1 - STUDENT DETAILS
# =====================================================

if st.session_state.page == "details":

    st.markdown("""
    <div class="header">
        <h1>🎓 SMARTMARK</h1>
        <p>Student Examination Performance Analyzer</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("👨‍🎓 Student Information")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input(
            "Student Name",
            placeholder="Enter student name"
        )

    with col2:
        register_number = st.text_input(
            "Register Number",
            placeholder="Enter register number"
        )

    st.markdown("---")

    st.subheader("📚 Enter Subject Marks")

    col1, col2 = st.columns(2)

    with col1:

        maths = st.number_input(
            "📐 Discrete Mathematics",
            min_value=0,
            max_value=100,
            value=0
        )

        dsa = st.number_input(
            "💻 Data Structure & Algorithm",
            min_value=0,
            max_value=100,
            value=0
        )

        programming = st.number_input(
            "🐍 Programming",
            min_value=0,
            max_value=100,
            value=0
        )

    with col2:

        data_science = st.number_input(
            "📊 Foundation of Data Science",
            min_value=0,
            max_value=100,
            value=0
        )

        dpco = st.number_input(
            "🖥️ DPCO",
            min_value=0,
            max_value=100,
            value=0
        )

    st.markdown("---")

    if st.button("🚀 Analyze My Performance", use_container_width=True):

        if name.strip() == "" or register_number.strip() == "":
            st.error("⚠️ Please enter Student Name and Register Number.")

        else:

            marks = {
                "Discrete Mathematics": maths,
                "Foundation of Data Science": data_science,
                "Data Structure & Algorithm": dsa,
                "DPCO": dpco,
                "Programming": programming
            }

            st.session_state.student_data = {
                "name": name,
                "register": register_number,
                "marks": marks
            }

            st.session_state.page = "analysis"

            st.rerun()

# =====================================================
# PAGE 2 - PERFORMANCE ANALYSIS
# =====================================================

else:

    data = st.session_state.student_data

    name = data["name"]
    register_number = data["register"]
    marks = data["marks"]

    total = sum(marks.values())
    average = total / len(marks)

    strong_subject = max(marks, key=marks.get)
    weak_subject = min(marks, key=marks.get)

    highest_mark = max(marks.values())
    lowest_mark = min(marks.values())

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    if lowest_mark >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    # -------------------------------------------------
    # HEADER
    # -------------------------------------------------

    st.markdown("""
    <div class="header">
        <h1>📊 Performance Analysis</h1>
        <p>Personalized Academic Performance Report</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="card">
        <h2>👨‍🎓 {name}</h2>
        <p>🆔 Register Number: <b>{register_number}</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # METRICS
    # -------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🏆 Total Marks",
            f"{total}/500"
        )

    with c2:
        st.metric(
            "📈 Average",
            f"{average:.2f}"
        )

    with c3:
        st.metric(
            "🎓 Grade",
            grade
        )

    with c4:
        st.metric(
            "✅ Result",
            result
        )

    st.markdown("---")

    # -------------------------------------------------
    # STRONG & NEEDS IMPROVEMENT
    # -------------------------------------------------

    c1, c2 = st.columns(2)

    with c1:

        st.markdown(
            f"""
            <div class="success-card">
            <h3>💪 Strong Subject</h3>
            <h2>{strong_subject}</h2>
            <p>Highest Mark: <b>{highest_mark}/100</b></p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            f"""
            <div class="warning-card">
            <h3>📚 Needs Improvement</h3>
            <h2>{weak_subject}</h2>
            <p>Current Mark: <b>{lowest_mark}/100</b></p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # -------------------------------------------------
    # PERFORMANCE CHART
    # -------------------------------------------------

    st.subheader("📈 Subject-wise Performance")

    chart_data = {
        "Subject": list(marks.keys()),
        "Marks": list(marks.values())
    }

    fig = px.bar(
        chart_data,
        x="Subject",
        y="Marks",
        text="Marks",
        color="Marks",
        color_continuous_scale="Viridis",
        title="Your Subject Marks"
    )

    fig.update_layout(
        yaxis=dict(range=[0, 100]),
        plot_bgcolor="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # -------------------------------------------------
    # PERFORMANCE SUMMARY
    # -------------------------------------------------

    st.subheader("📝 Performance Summary")

    if result == "PASS":

        st.success(
            f"🎉 {name}, you have successfully passed the examination "
            f"with an average of {average:.2f}."
        )

    else:

        st.warning(
            f"⚠️ {name}, some subjects need more attention. "
            f"Focus especially on {weak_subject}."
        )

    st.info(
        f"💡 Your strongest performance is in **{strong_subject}** "
        f"with {highest_mark}/100. "
        f"More attention can be given to **{weak_subject}**."
    )

    st.markdown("---")

    # -------------------------------------------------
    # BACK BUTTON
    # -------------------------------------------------

    if st.button("⬅️ Analyze Another Student"):
        st.session_state.page = "details"
        st.session_state.student_data = None
        st.rerun()

    st.markdown("""
    <div class="footer">
        🎓 <b>SMARTMARK</b><br>
        Student Examination Performance Analyzer
    </div>
    """, unsafe_allow_html=True)

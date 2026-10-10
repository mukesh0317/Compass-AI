import streamlit as st
import pandas as pd
import plotly.express as px
from ml.bkt_model import estimate_mastery, recommend_practice

st.set_page_config(page_title="COMPASS AI", page_icon="🎓", layout="wide")

st.markdown("""
<style>
.block-container {padding-top: 1.7rem; max-width: 1200px;}
.hero {padding: 1.4rem 1.6rem; border-radius: 18px; background: linear-gradient(120deg,#13243a,#245c74); color: white;}
.hero h1 {color: white; margin-bottom: .25rem;}
.hero p {color: #e2eef4; font-size: 1.05rem;}
.small-muted {color: #6b7280; font-size: .9rem;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>COMPASS AI</h1>
<p>Move beyond marks. Understand mastery. Personalize the learning journey.</p>
</div>
""", unsafe_allow_html=True)
st.write("Analyze assessment responses, estimate topic-level mastery, and discover what to practice next.")

with st.sidebar:
    st.header("Student workspace")
    student_name = st.text_input("Student name", "Demo Student")
    st.caption("Demo mode uses sample assessment responses. Avoid entering sensitive personal data.")
    st.divider()
    st.subheader("BKT model settings")
    p_learn = st.slider("Learning probability", 0.01, 0.50, 0.15, 0.01)
    p_guess = st.slider("Guess probability", 0.01, 0.40, 0.20, 0.01)
    p_slip = st.slider("Slip probability", 0.01, 0.40, 0.10, 0.01)
    p_prior = st.slider("Initial mastery probability", 0.05, 0.95, 0.20, 0.05)

@st.cache_data
def load_demo_data():
    return pd.read_csv("data/sample_assessments.csv")

demo = load_demo_data()
topics = sorted(demo["skill"].unique())

st.subheader("1. Assessment evidence")
st.write("Choose a sample learner profile or upload your own CSV with columns: `student`, `skill`, `correct` (0 or 1).")
uploaded = st.file_uploader("Upload assessment CSV (optional)", type=["csv"])
if uploaded:
    try:
        data = pd.read_csv(uploaded)
        required = {"student", "skill", "correct"}
        if not required.issubset(data.columns):
            st.error("CSV must contain these columns: student, skill, correct.")
            st.stop()
        data["correct"] = pd.to_numeric(data["correct"], errors="coerce")
        data = data.dropna(subset=["student", "skill", "correct"])
        data = data[data["correct"].isin([0, 1])]
        if data.empty:
            st.error("No valid rows found. Ensure correct contains only 0 or 1.")
            st.stop()
    except Exception as exc:
        st.error(f"Could not read CSV: {exc}")
        st.stop()
else:
    data = demo.copy()

students = sorted(data["student"].astype(str).unique())
selected_student = st.selectbox("Select student", students, index=students.index(student_name) if student_name in students else 0)
student_data = data[data["student"].astype(str) == selected_student].copy()

with st.expander("View selected student's assessment responses"):
    st.dataframe(student_data, use_container_width=True, hide_index=True)

st.subheader("2. Competency profile")
rows = []
for skill in sorted(data["skill"].astype(str).unique()):
    attempts = student_data[student_data["skill"].astype(str) == skill]["correct"].astype(int).tolist()
    if attempts:
        mastery = estimate_mastery(attempts, p_learn=p_learn, p_guess=p_guess, p_slip=p_slip, p_prior=p_prior)
        accuracy = sum(attempts) / len(attempts)
        rows.append({"Skill": skill, "Estimated mastery (%)": round(mastery * 100, 1),
                     "Observed accuracy (%)": round(accuracy * 100, 1), "Attempts": len(attempts)})
    else:
        rows.append({"Skill": skill, "Estimated mastery (%)": 0.0, "Observed accuracy (%)": 0.0, "Attempts": 0})

profile = pd.DataFrame(rows)
if profile.empty:
    st.info("No assessment responses found for this student.")
    st.stop()

avg_mastery = profile["Estimated mastery (%)"].mean()
attempt_count = int(profile["Attempts"].sum())
weak_count = int((profile["Estimated mastery (%)"] < 60).sum())
c1, c2, c3 = st.columns(3)
c1.metric("Average estimated mastery", f"{avg_mastery:.1f}%")
c2.metric("Assessment attempts", attempt_count)
c3.metric("Skills needing practice", weak_count)

fig = px.bar(profile.sort_values("Estimated mastery (%)"), x="Estimated mastery (%)", y="Skill",
             orientation="h", color="Estimated mastery (%)", range_x=[0, 100],
             title="Estimated mastery by skill", text="Estimated mastery (%)",
             color_continuous_scale="Teal")
fig.update_layout(coloraxis_showscale=False, xaxis_title="Estimated mastery (%)", yaxis_title="")
st.plotly_chart(fig, use_container_width=True)

with st.expander("Compare estimated mastery with observed accuracy"):
    compare = profile.melt(id_vars=["Skill"], value_vars=["Estimated mastery (%)", "Observed accuracy (%)"],
                           var_name="Measure", value_name="Percent")
    compare_fig = px.bar(compare, x="Skill", y="Percent", color="Measure", barmode="group",
                         range_y=[0, 100], title="Model estimate vs. observed accuracy")
    st.plotly_chart(compare_fig, use_container_width=True)

st.subheader("3. Recommended next steps")
recommendations = recommend_practice(profile.to_dict("records"))
if recommendations:
    for rec in recommendations:
        with st.container(border=True):
            st.markdown(f"**{rec['skill']}** — {rec['level']}")
            st.write(rec["recommendation"])
            st.caption(f"Estimated mastery: {rec['mastery']:.1f}% · Attempts: {rec['attempts']}")
else:
    st.success("No skill gaps detected in this sample. Continue with mixed practice to maintain mastery.")

st.subheader("4. Export competency report")
csv = profile.to_csv(index=False).encode("utf-8")
st.download_button("Download competency report (CSV)", data=csv,
                   file_name="compass_ai_competency_report.csv", mime="text/csv")

st.caption("Research prototype: BKT estimates are illustrative and depend on model assumptions. This demo is not a validated grading or high-stakes decision system.")

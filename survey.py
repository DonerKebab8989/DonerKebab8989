import streamlit as st

def set_style():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

set_style()

st.title("Quiz")
st.subheader("Please answer the following questions based on your first impression.")
q1 = ["Bright songs", "Dark songs", "Not sure / Either is fine"]
selection1 = st.segmented_control(
    "🎤Regardless of the lyrics, which kind of vibe do you prefer when you listen?", q1, selection_mode="single", key="q1"
)
st.markdown("""
<style>
div[data-testid="stSegmentedControl"][aria-label="q1"] button {
    color: black !important;
}
</style>
""", unsafe_allow_html=True
)
st.session_state["answer1"] = selection1
q2 = ["Romance", "Friendship", "School", "Youth", "Cheering / Motivation", "Family", "Seasons / Events / Nature", "Goodbye / Farewell", "Anime", "Drama / Movies"]
selection2 = st.segmented_control(
    "🎤 What kind of music themes do you like? (You can choose more than one♪)", q2, selection_mode="multi", key="q2"
)
st.markdown("""
<style>
div[data-testid="stSegmentedControl"][aria-label="q2"] button {
    color: black !important;
}
</style>
""", unsafe_allow_html=True
)
st.session_state["answer2"] = selection2
q3 = ["Upbeat", "Slow", "Rhythmic", "None of these"]
selection3 = st.segmented_control(
    "🎤What tempo do you like?", q3, selection_mode="single", key="q3"
)
st.markdown("""
<style>
div[data-testid="stSegmentedControl"][aria-label="q3"] button {
    color: black !important;
}
</style>
""", unsafe_allow_html=True
)
st.session_state["answer3"] = selection3
st.page_link("result.py", label="→ See your results here")
import streamlit as st

def set_style():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

set_style()

home = st.Page("home.py", title="ホーム")
survey = st.Page("survey.py", title="診断テスト")
result = st.Page("result.py", title="結果")

nav = st.navigation([home, survey, result])
nav.run()
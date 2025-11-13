import streamlit as st

st.title("ホーム")
st.header("わはははは")

home = st.Page("AimerAPP.py", title="ホーム")
survey = st.Page("survey.py", title="診断テスト")
result = st.Page("result.py", title="結果")
fav = st.Page("fav.py", title="オススメ")

nav = st.navigation([home, survey, result, fav])
nav.run()
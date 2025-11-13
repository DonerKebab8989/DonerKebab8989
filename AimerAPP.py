import streamlit as st

home = st.Page("home.py", title="ホーム")
survey = st.Page("survey.py", title="診断テスト")
result = st.Page("result.py", title="結果")
fav = st.Page("fav.py", title="オススメ")

nav = st.navigation([home, survey, result, fav])
nav.run()
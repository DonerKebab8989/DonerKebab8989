import streamlit as st

st.title("診断テスト")
st.subheader("以下の質問に直感でお答えください。")
q1 = ["明るい曲", "暗い曲", "どちらともいえない"]
selection1 = st.segmented_control(
    "🎤歌詞の意味は関係なく、聞いた感じの雰囲気はどっちが好き？", q1, selection_mode="single"
)
st.session_state["answer1"] = selection1
q2 = ["恋愛", "友情", "学校", "青春", "応援", "家族", "季節・イベント・自然", "別れ", "アニメ", "ドラマ・映画"]
selection2 = st.segmented_control(
    "🎤好きな音楽のジャンルは？複数選択できます♪", q2, selection_mode="multi"
)
st.session_state["answer2"] = selection2
q3 = ["アップテンポ", "ゆっくり", "リズミカル", "あてはまるものはない"]
selection3 = st.segmented_control(
    "🎤どんなテンポが好き？", q3, selection_mode="single"
)
st.session_state["answer3"] = selection3
st.page_link("result.py", label="→診断結果はこちら")
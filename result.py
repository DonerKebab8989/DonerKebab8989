import streamlit as st

def set_style():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

set_style()

st.title("診断結果")
songs = {
    "六等星の夜": {
        "雰囲気": "Dark songs",
        "ジャンル": ["Romance", "Friendship", "Youth", "Family", "Goodbye / Farewell", "Seasons / Events / Nature"],
        "テンポ": "Slow",
        "紹介": "Aimerのデビューソング",
        "リンク": "https://youtu.be/jgSyul7n-8M?si=LjHc2VV1FExhyqSc"
    },
    "SPARK-AGAIN": {
        "雰囲気": "Not sure / Either is fine",
        "ジャンル": ["Anime", "Cheering / Motivation", "Friendship", "Youth", "Romance"],
        "テンポ": "Upbeat",
        "紹介": "『炎炎ノ消防隊 弐ノ章』オープニング主題歌",
        "リンク": "https://youtu.be/dZ0Jt1zYj7g?si=e1uVX-AfCT8smD7M"
    },
    "Re:pray": {
        "雰囲気": "Bright songs",
        "ジャンル": ["Romance", "Seasons / Events / Nature", "Goodbye / Farewell", "Youth", "Anime"],
        "テンポ": "None of these",
        "紹介": "アニメ『BLEACH』エンディング主題歌",
        "リンク": "https://music.youtube.com/watch?v=_2Qx1I8tlxM&si=dqh7-HgJ651rsGRe"
    },
    "思い出は綺麗で": {
        "雰囲気": "Bright songs",
        "ジャンル": ["Family", "Youth", "Goodbye / Farewell"],
        "テンポ": "None of these",
        "紹介": "家族を悼む切なくも優しい曲",
        "リンク": "https://youtu.be/brZxXTG7XR8?si=HuXYw5nI1wS6nBK6"
    },
    "STAND-ALONE": {
        "雰囲気": "Dark songs",
        "ジャンル": ["Romance", "Drama / Movies", "Goodbye / Farewell", "Seasons / Events / Nature", "Family"],
        "テンポ": "Rhythmic",
        "紹介": "TVドラマ『あなたの番です』主題歌",
        "リンク": "https://youtu.be/wVMPqFb5Iy8?si=L-Zdmew881-G8nd_"
    },
    "残響賛歌": {
        "雰囲気": "Bright songs",
        "ジャンル": ["Youth", "Cheering / Motivation", "Anime", "Seasons / Events / Nature"],
        "テンポ": "Upbeat",
        "紹介": "TVアニメ『鬼滅の刃 遊郭編』オープニング主題歌",
        "リンク": "https://youtu.be/tLQLa6lM3Us?si=vmLeAZNZ4NVaedwO"
    },
    "太陽が昇らない世界 - A World Where the Sun Never Rises": {
        "雰囲気": "Dark songs",
        "ジャンル": ["Anime", "Seasons / Events / Nature", "Goodbye / Farewell", "Cheering / Motivation"],
        "テンポ": "Upbeat",
        "紹介": "劇場版『鬼滅の刃 無限城編 第一章 猗窩座再来』主題歌",
        "リンク": "https://youtu.be/DJOf0XtVpkI?si=7xu7jgYez18N3V9e"
    },
    "カタオモイ": {
        "雰囲気": "Bright songs",
        "ジャンル": ["Romance", "Goodbye / Farewell", "Youth"],
        "テンポ": "Rhythmic",
        "紹介": "ロングヒットした片想いのラブソング",
        "リンク": "https://youtu.be/kxs9Su_mbpU?si=F22AbfRxjef-JTnt"
    },
    "Brave Shine": {
        "雰囲気": "Not sure / Either is fine",
        "ジャンル": ["Anime", "Cheering / Motivation", "Seasons / Events / Nature"],
        "テンポ": "None of these",
        "紹介": "TVアニメ『Fate/staynight [UBW]』(by Ufotable)オープニング主題歌",
        "リンク": "https://youtu.be/VQ2D8rZljwU?si=LfxwqJOx2dwSf1yJ"
    },
    "蝶々結び": {
        "雰囲気": "Not sure / Either is fine",
        "ジャンル": ["Romance", "Youth", "Seasons / Events / Nature", "Anime"],
        "テンポ": "Slow",
        "紹介": "野田洋次郎が楽曲提供したヒットソング",
        "リンク": "https://youtu.be/Du_5wIB26-M?si=QtCI2JvbewFPtvN1"
    },
    "茜さす": {
        "雰囲気": "Not sure / Either is fine",
        "ジャンル": ["Romance", "Goodbye / Farewell", "Seasons / Events / Nature", "Anime", "Friendship", "Family"],
        "テンポ": "Slow",
        "紹介": "TVアニメ『夏目友人帳』エンディング主題歌",
        "リンク": "https://youtu.be/bN1t3-2X3aM?si=-zgFD7hrzfVKPbi8"
    },
    "朝が来る": {
        "雰囲気": "Dark songs",
        "ジャンル": ["Cheering / Motivation", "Seasons / Events / Nature", "Anime"],
        "テンポ": "Rhythmic",
        "紹介": "TVアニメ『鬼滅の刃 遊郭編』エンディング主題歌",
        "リンク": "https://youtu.be/QORbTrXHpsA?si=ErPjSQNm-Ig-Yq_B"
    },
    "星屑ビーナス": {
        "雰囲気": "Dark songs",
        "ジャンル": ["Romance", "Goodbye / Farewell", "Cheering / Motivation", "Friendship", "Drama / Movies"],
        "テンポ": "Slow",
        "紹介": "TVドラマ『恋なんて贅沢が私に落ちてくるのだろうか？』主題歌",
        "リンク": "https://youtu.be/sMy1lK1L67g?si=-mLccFm7YAhLfyyv"
    },
    "遥か": {
        "雰囲気": "Not sure / Either is fine",
        "ジャンル": ["Romance", "Drama / Movies", "Seasons / Events / Nature"],
        "テンポ": "Slow",
        "紹介": "実写版『からかい上手の高木さん』主題歌",
        "リンク": "https://music.youtube.com/watch?v=HJhYU0TbHKI&si=JwaPIs2vkrRuUDGK"
    },
    "コイワズライ": {
        "雰囲気": "Bright songs",
        "ジャンル": ["Romance", "Cheering / Motivation", "Goodbye / Farewell", "Drama / Movies", "Youth"],
        "テンポ": "Rhythmic",
        "紹介": "恋愛リアリティーショー『白雪とオオカミくんには騙されない❤』主題歌",
        "リンク": "https://youtu.be/c2tuxS3Pcto?si=cxinY4Y8nXKAkUyT"
    },
    "RE:I AM": {
        "雰囲気": "Dark songs",
        "ジャンル": ["Goodbye / Farewell", "Anime", "Cheering / Motivation", "Seasons / Events / Nature"],
        "テンポ": "None of these",
        "紹介": "OVAアニメ『機動戦士ガンダムUC episode 6「宇宙と地球と」』オープニング主題歌",
        "リンク": "https://music.youtube.com/watch?v=hp7LCijEVaU&si=72NehfhcUl3ZFvWm"
    },
    "I beg you": {
        "雰囲気": "Dark songs",
        "ジャンル": ["Romance", "Anime", ""],
        "テンポ": "Rhythmic",
        "紹介": "劇場版『Fate/staynight [HF]Ⅱ』主題歌",
        "リンク": "https://youtu.be/pCC6qbAnX00?si=UyYGLN_HS2uFVA9e"
    },
    "Ref:rain": {
        "雰囲気": "Not sure / Either is fine",
        "ジャンル": ["Romance", "Anime", "Goodbye / Farewell", "Youth", "Seasons / Events / Nature", "School"],
        "テンポ": "Slow",
        "紹介": "TVアニメ『恋は雨上がりのように』エンディング主題歌",
        "リンク": "https://youtu.be/mvkbCZfwWzA?si=Mt9HYA95fggzCyEP"
    },
    "Deep down": {
        "雰囲気": "Dark songs",
        "ジャンル": ["Anime", "Goodbye / Farewell"],
        "テンポ": "Slow",
        "紹介": "TVアニメ『チェンソーマン』エンディング主題歌",
        "リンク": "https://youtu.be/X75Qy-GiW4Y?si=G3GfrhY-tf2KhGSg"
    },
    "季路": {
        "雰囲気": "Not sure / Either is fine",
        "ジャンル": ["Anime", "Seasons / Events / Nature"],
        "テンポ": "Slow",
        "紹介": "アニメ『魔道祖士』主題歌",
        "リンク": "https://youtu.be/M3J1KRD1H1Q?si=1KLsa-RqpLJtCJev"
    },
    "あなたに出会わなければ ～夏雪冬花～": {
        "雰囲気": "Dark songs",
        "ジャンル": ["Romance", "Anime", "Goodbye / Farewell", "Seasons / Events / Nature", "Family"],
        "テンポ": "Slow",
        "紹介": "TVアニメ『夏雪ランデブー』主題歌",
        "リンク": "https://youtu.be/HTgyE9vMIc0?si=6v5mCOJFVQmrrRys"
    },
    "ポラリス": {
        "雰囲気": "Not sure / Either is fine",
        "ジャンル": ["Romance", "Family", "Cheering / Motivation", "Seasons / Events / Nature"],
        "テンポ": "Slow",
        "紹介": "ひとりで寂しいとき、聴くのにピッタリ♪",
        "リンク": "https://youtu.be/BZPWmJYI_a4?si=5y7gPzZmY8-TSxHR"
    },
    "あてもなく": {
        "雰囲気": "Not sure / Either is fine",
        "ジャンル": ["Family", "Anime", "Cheering / Motivation", "Friendship", "Youth"],
        "テンポ": "Rhythmic",
        "紹介": "TVアニメ『王様ランキング』エンディング主題歌",
        "リンク": "https://youtu.be/PLCO7eIJHh8?si=tHEdcCb_iOZabdUi"
    },
    "LAST STARDUST": {
        "雰囲気": "Not sure / Either is fine",
        "ジャンル": ["Anime", "Goodbye / Farewell", "Cheering / Motivation"],
        "テンポ": "Slow",
        "紹介": "TVアニメ『Fate/staynight [UBW]』挿入歌",
        "リンク": "https://music.youtube.com/watch?v=t9FY1YRY-ZQ&si=3403YuT_0xgTnI5e"
    },
    "春はゆく": {
        "雰囲気": "Dark songs",
        "ジャンル": ["Anime", "Seasons / Events / Nature", "Romance"],
        "テンポ": "Slow",
        "紹介": "劇場版『Fate/staynight [HF]Ⅲ』主題歌",
        "リンク": "https://youtu.be/ekP7VLeXnqY?si=cLTS5i4KfAC-_qQS"
    },
    "ONE": {
        "雰囲気": "Bright songs",
        "ジャンル": ["Youth", "Cheering / Motivation", "School", "Romance", "Friendship"],
        "テンポ": "Upbeat",
        "紹介": "カーリング日本代表CMにも起用された応援ソング",
        "リンク": "https://youtu.be/FeSqXFgzCZk?si=EnAMFVy-gMspdYd0"
    },
    "everlasting snow": {
        "雰囲気": "Bright songs",
        "ジャンル": ["Seasons / Events / Nature", "Romance", "Cheering / Motivation"],
        "テンポ": "Slow",
        "紹介": "心あたたまるクリスマスソング",
        "リンク": "https://youtu.be/T-WH1qv1YJM?si=4aVDXRUcJBP48K8g"
    },
    "Black Bird": {
        "雰囲気": "Dark songs",
        "ジャンル": ["Drama / Movies", "Romance", "Goodbye / Farewell"],
        "テンポ": "Upbeat",
        "紹介": "実写劇場版『累-かさね-』主題歌",
        "リンク": "https://youtu.be/ax8DmYyx9Ms?si=y5Pjv5z3dqBH-ZD5"
    },
    "花びらたちのマーチ": {
        "雰囲気": "Bright songs",
        "ジャンル": ["School", "Romance", "Goodbye / Farewell", "Youth", "Cheering / Motivation"],
        "テンポ": "Rhythmic",
        "紹介": "切なくも前向きになれる学園ラブソング",
        "リンク": "https://music.youtube.com/watch?v=QLsNCsu6Lio&si=z0Ln50fgbj9SrdA5"
    }
}
user = {
    "雰囲気": st.session_state["answer1"],
    "ジャンル": st.session_state["answer2"],
    "テンポ": st.session_state["answer3"]
}
scores = {}
for title, tags in songs.items():
    score = 0
    if user["雰囲気"] == tags["雰囲気"]:
        score += 1
    genres = set(user["ジャンル"]) & set(tags["ジャンル"])
    score += len(genres)
    if user["テンポ"] == tags["テンポ"]:
        score += 1
    scores[title] = score
sorted_songs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
best = sorted_songs[0]
others = sorted_songs[1:4]
best_title = best[0]
best_score = best[1]
best_info = songs[best_title]
st.header("🎉 Your Best Song")
st.markdown(f"""
<div class="card">
    <h2>{best_title}</h2>
    <p>{best_info['紹介']}</p>
    <a href="{best_info['リンク']}" class="custom-link" target="_blank">
        To Listeng by YouTube
    </a>
</div>
""", unsafe_allow_html=True)
st.subheader("💡 others")
for title, score in others:
    info = songs[title]
    st.markdown(f"""
<div class="card">
    <h3>{title}</h3>
    <p>{info['紹介']}</p>
    <a href="{info['リンク']}" class="custom-link" target="_blank">
        ▶ YouTubeで聴く
    </a>
</div>
""", unsafe_allow_html=True)
st.page_link("survey.py", label="→one more")
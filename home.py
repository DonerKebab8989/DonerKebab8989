import streamlit as st

def set_style():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

set_style()

st.title("Let’s Find Your Favorite Aimer Song♪")
st.header("Who Is Aimer?")
st.markdown("""
Aimer is a female J-pop artist known for her work on theme songs for dramas, movies, and anime.

For example, her song “Koiwazurai” was featured in the romance reality show *Ookami Series*, “Zankyou Sanka” was used in the anime *Demon Slayer: Kimetsu no Yaiba*, and “STAND-ALONE” appeared in the suspense drama *Your Turn to Kill*—just to name a few.
She’s a well-known singer who has performed theme songs for many popular titles!

And her one-of-a-kind husky voice is simply irresistible✨

You’ve probably heard at least one of her hit songs before.
But I want to share even more of Aimer’s charm and help you discover more of her amazing music!!

Of course, I’m not saying you have to listen to every single one of her countless songs
(though honestly, I’d love for you to!).
That’s why this app will help you figure out what kind of Aimer songs might suit you best♪

In this app, we’ll analyze your preferences and introduce you to songs we recommend just for you!!
            """)
st.page_link("survey.py", label="→Take the quiz here")
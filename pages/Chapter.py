import streamlit as st
VIDEO_URL = "https://www.w3schools.com/html/mov_bbb.mp4"

# Define your chapters (label -> start time in seconds)
CHAPTERS = {
    "Intro": 0,
    "Scene A": 2,
    "Scene B": 5,
    "Scene C": 7,
}

st.title("🎬 Video Chapters ")

# Keep current chapter time in session state
st.session_state.setdefault("chapter_time", 0)

# Main player (jumps to selected chapter)
with st.container(width=800):
    cols = st.columns(len(CHAPTERS),gap='medium')
    for i, (label, t) in enumerate(CHAPTERS.items()):
        with cols[i]:
            if st.button(label):
                st.session_state["chapter_time"] = t
    st.video(VIDEO_URL, start_time=st.session_state["chapter_time"])
    st.caption(f"Current chapter start: {st.session_state['chapter_time']}s")
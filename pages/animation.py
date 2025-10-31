import streamlit as st
from pathlib import Path

VIDEO_URL = "https://youtu.be/uzumDxZMDwU"

# # Define your chapters (label -> start time in seconds)
# CHAPTERS = {
#     "Intro": 0,
#     "Scene A": 2,
#     "Scene B": 5,
#     "Scene C": 7,
# }


st.title("Animation")


ASSETS = Path("assets")

# VIDEO_PATH = ASSETS / "Shanghai_Lens_Moive.mp4"
AUDIO_TRACKS = {
    "Kids Song": ASSETS / "kids_song.mp3", 
    "Gu Feng":   ASSETS / "ancient_song.mp3", 
}


tab1, tab2, tab3= st.tabs(["Video", "Audio", "3D Model"])
with tab1:
    st.header("🎬 Video")
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.video(str(VIDEO_URL), start_time=0)
    # with st.container(width=800,border=False):
    #     st.video("https://youtu.be/uzumDxZMDwU", loop=True)
        
with tab2:    
    st.header("🔊 Audio")
    choice = st.selectbox("Track", list(AUDIO_TRACKS.keys()), index=0)
    audio_file = AUDIO_TRACKS[choice]
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.audio(str(audio_file))
    # with st.container(width=800):
    #     st.audio('https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg',
    #          loop=True)

with tab3:    
    st.header("🧸 3D Model")

    scenes = [
        {"img": 'assets/3D/oriental_pearl_tower.png', "text": "Oriental Pearl Tower"},  
        {"img": "assets/3D/koala.png", "text": "Koala"},
        {"img": "assets/3D/shikumen.png", "text": "Shikumen"},
        {"img": "assets/3D/xiaolongbao.png", "text": "Xiaolongbao"}
    ]

    spacer1, col1, col2, col3, col4, spacer2 = st.columns(
        [0.5, 4, 4, 4, 4, 0.5],
        gap="large"
    )

    with col1:
        st.image(scenes[0]["img"], use_container_width=True)
        st.caption(scenes[0]["text"])

    with col2:
        st.image(scenes[1]["img"], use_container_width=True)
        st.caption(scenes[1]["text"])

    with col3:
        st.image(scenes[2]["img"], use_container_width=True)
        st.caption(scenes[2]["text"])

    with col4:
        st.image(scenes[3]["img"], use_container_width=True)
        st.caption(scenes[3]["text"])





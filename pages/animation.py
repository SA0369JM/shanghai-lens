import streamlit as st
# VIDEO_URL = "https://www.w3schools.com/html/mov_bbb.mp4"

# # Define your chapters (label -> start time in seconds)
# CHAPTERS = {
#     "Intro": 0,
#     "Scene A": 2,
#     "Scene B": 5,
#     "Scene C": 7,
# }


st.title("Animation")

tab1, tab2, tab3= st.tabs(["Video", "Audio", "3D Model"])
with tab1:
    st.header("🎬 Video")
    st.image('assets/comming_soon.png')
    # with st.container(width=800,border=False):
    #     st.video("assets/star.mp4", loop=True,subtitles="assets/sub.vtt")
        
with tab2:    
    st.header("🔊 Audio")
    st.image('assets/comming_soon.png')
    # with st.container(width=800):
    #     st.audio('https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg',
    #          loop=True)

with tab3:    
    st.header("🧸 3D Model")
    st.subheader("continuing ... more coming soon")

    scenes = [
        {"img": 'assets/3D/oriental_pearl_tower.png', "text": "Oriental Pearl Townel (working on colour)"},  
        {"img": "assets/3D/koala.png","text": "koala (work on change the outlook)" },
    ]

    spacer1, col1, col2, spacer2 = st.columns([0.5,4,4,0.5], gap="large")
    with col1:
        st.image(scenes[0]["img"], use_container_width=True)  
        st.caption(scenes[0]["text"])

    with col2:
        st.image(scenes[1]["img"], use_container_width=True)
        st.caption(scenes[1]["text"])
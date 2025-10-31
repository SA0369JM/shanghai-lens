
# pages/Poster.py
import streamlit as st
import time

with st.container(width='stretch',height="content"):
    st.image('assets/banner.png')

    
st.title("📖 Storyboard")

# st.write("A journey begins ...")
# {"img": "assets/COMP5415_Scene_1.png", 
#      "text": "A journey begins ... Koala(represent myself as I came to Austraia in an early years)"},

spacer1, top_col1, top_col2, spacer2 = st.columns([0.5,5,4,1], gap="large")

with top_col1:
    st.image("assets/scenes/COMP5415_Scene_1.png", use_container_width=True)

with top_col2:
    st.write("A journey begins ...")
    st.caption("""
    Koala is a repersentative of myself as I came to 
    Sydney in an early age. It arrives in front of 
    a traditional Shanghai SHIKUMEN. 
             
    As the koala gently opens the door, the scene leaps to the eye initiated the lens of Shanghai...
    """)


scenes = [
    {"img": "assets/scenes/COMP5415_Scene_2.png", 
     "text": "The walk to CHENGHUANGMIAO. Jiuqu Bridge is a must-cross each time with a no walk back tradition, which symbolizing tradition and fortune. "},

    {"img": "assets/scenes/COMP5415_Scene_3.png", 
     "text": "At the end of the bridge, the famous Nanxiang steamed buns await, offering a delicious taste that completes the journey. "},

    {"img": "assets/scenes/COMP5415_Scene_4.png", 
     "text": "A city walk along the Huangpu River to admire the Bund skyline lit up at night. Dinner is enjoyed high above the city at Shanghai Tower, indulging in a seafood feast. Of course, hairy crabs are indispensable on the dinner table."},
    
    {"img": "assets/scenes/COMP5415_Scene_5.png", 
     "text": "The journey came to close with the breathtaking Disney fireworks, lighting up the night sky and bringing this Shanghai journey to a magical ending."},
]

spacer1, col1, col2, spacer2 = st.columns([0.5,4,4,0.5], gap="large")
with col1:
    st.image(scenes[0]["img"], use_container_width=True)  
    st.caption(scenes[0]["text"])

with col2:
    st.image(scenes[1]["img"], use_container_width=True)
    st.caption(scenes[1]["text"])


spacer3, col3, col4, spacer4 = st.columns([0.5,4,4,0.5], gap="large")
with col3:
    st.image(scenes[2]["img"], use_container_width=True)
    st.caption(scenes[2]["text"])
with col4:
    st.image(scenes[3]["img"], use_container_width=True)
    st.caption(scenes[3]["text"])
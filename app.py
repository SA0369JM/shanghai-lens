
# app.py
# -*- coding: utf-8 -*-
#Create an entry point script that defines and connects your pages
import streamlit as st

st.set_page_config(
    page_title="COMP4415/5415", #title on  the tab
    page_icon="🎬", 
    layout="wide")

with st.sidebar:
    st.code('''st.image('assets/logo.png')''')
    st.image('assets/logo.png')

pages = {
    "Text": [
        st.Page("pages/4_text.py", title="Text"),
    ],
    "Layout": [
        st.Page("pages/Cols.py", title="Columns"),
        st.Page("pages/Tabs.py", title="Tabs"),
        st.Page("pages/Container.py", title="Container"),
    ],
    "Images": [
        st.Page("pages/Poster.py", title="Poster"),
        st.Page("pages/Story.py", title="Storyboard"),
        st.Page("pages/Gallery.py", title="Gallery"),
        st.Page("pages/banner.py", title="Banner"),
        st.Page("pages/Image_map.py", title="Image Map"),

    ],
    "Audio": [
        st.Page("pages/Audio.py", title="Audio"),
    ],
    "Videos": [
        st.Page("pages/2_Video.py", title="Animation"),
        st.Page("pages/Chapter.py", title="Video Chapter"),
    ],
    
}

po=st.sidebar.selectbox("Navigation Bar", ["top", "sidebar", "hidden"], key="NP")

pg = st.navigation(pages,position=po)
pg.run()








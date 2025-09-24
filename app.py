
# app.py
# -*- coding: utf-8 -*-
#Create an entry point script that defines and connects your pages
import streamlit as st

st.set_page_config(
    page_title="Shanghai Lens", #title on the tab
    page_icon="📷", 
    layout="wide")

with st.sidebar:
    st.image('assets/logo.png', caption="@Shanghai Lens · Amy Shi")
    st.markdown("")

pages = {
    "Overview": [
        st.Page("pages/story.py", title="Story"),
    ],
    "Shanghai": [
        st.Page("pages/map.py", title="Map"),
        st.Page("pages/gallery.py", title="Gallery"),
        st.Page("pages/shanghai_panorama.py", title="Shanghai Panorama"),
    ],
    "Project": [
        st.Page("pages/web_design.py", title="Web Design"),
        st.Page("pages/banner.py", title="Banner"),
        st.Page("pages/poster.py", title="Poster"),
        st.Page("pages/animation.py", title="Animation"),

    ]   
}

# po=st.sidebar.selectbox("Navigation Bar", ["top", "sidebar", "hidden"], key="NP")

# pg = st.navigation(pages,position=po)
pg = st.navigation(pages,position="top")
pg.run()








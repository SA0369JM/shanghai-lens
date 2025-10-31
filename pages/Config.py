import streamlit as st
st.title("Config")

option = st.selectbox(
    "How would you like your navigation?",
    ("top", "sidebar", "hidden"),
)

st.write("You selected:", option)

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
    "Config": [
        st.Page("pages/Config.py", title="Config"),
   
    ],
    
}


pg = st.navigation(pages,position=option)

pg.run()
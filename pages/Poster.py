
# pages/Poster.py
import streamlit as st
import time

st.set_page_config(page_title="Poster · Multimedia Container", page_icon="🖼️", layout="wide")
st.title('Poster')
st.code('''
tab1, tab2 = st.tabs(["JAWS", "AVATAR"])
with tab1:
    st.header("JAWS")
    with st.container(border=True,width=600,height=800):
        st.image("assets/jaws.jpg")
with tab2:    
    st.header("Avatar")
    with st.container(width=600,height="content"):
        st.image("assets/avatar.jpg")
''',wrap_lines=True)

tab1, tab2 = st.tabs(["JAWS", "AVATAR"])
with tab1:
    st.header("JAWS")
    with st.container(border=True,width=600,height=800):
        st.image("assets/jaws.jpg")
with tab2:    
    st.header("Avatar")
    with st.container(width=600,height="content"):
        st.image("assets/avatar.jpg")


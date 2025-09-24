
# pages/Poster.py
import streamlit as st
import time

st.title('Poster')

st.subheader("🌟 Concept")
st.write("This is a small, muted caption (good for footnotes).")

st.divider()

with st.container(width=600,height="content"):
    st.image("assets/poster_ver3.png")



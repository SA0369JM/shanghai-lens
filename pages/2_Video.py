
# pages/2_Video.py
import streamlit as st
import base64

st.set_page_config(page_title="Video", page_icon="🎞️", layout="wide")
with st.container(width=800,border=False):
    st.video("assets/star.mp4", loop=True,subtitles="assets/sub.vtt")
with st.container(width=800,border=False):
    st.code('''
WEBVTT

0:00:01.000 --> 0:00:02.000
Look!

0:00:03.000 --> 0:00:05.000
Look at the pretty stars!

''')

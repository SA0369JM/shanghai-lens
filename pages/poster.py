
# pages/Poster.py
import streamlit as st
import time

st.title('Poster')

st.subheader("🌟 Concept")
st.write('''
         The poster functions as a promotional medium to showcase the cultural and modern charm of Shanghai, attracting audiences' attention while conveying both its iconic landmarks and local lifestyle.
         ''')
st.write('''
         The design integrates multiple symbolic elements:
         - Skyline: The Oriental Pearl Tower, Jin Mao Tower, World Financial Center, and Shanghai Tower represent Shanghai's global image and modernity. It is also echoes the banner.
         - Traditional Architecture: The illustration of classical pavilion structures connects the viewer with Shanghai's historical roots and cultural identity.
         - Food Elements: Steamed buns (xiaolongbao) and hairy crabs highlight the city's rich culinary culture, a vital part of local life.
         ''')

st.subheader("🪧 Slogan")
st.write ('''
          - "Through the Lens of Shanghai, More Than Scenery": emphasizes that Shanghai is not only about its breathtaking views but also about culture, traditions, and lived experiences.
          ''')

st.divider()

with st.container(width=600,height="content"):
    st.image("assets/poster_ver3.png")



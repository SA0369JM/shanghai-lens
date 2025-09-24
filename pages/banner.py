import streamlit as st

st.title("Banner")

st.subheader("🌟 Concept")
st.write('''
         This is a small, muted caption (good for footnotes).
         ''')

st.subheader("🪧 Slogan")
st.write ('''
          - "more than just scenery": 
          ''')

st.divider()



with st.container(width='stretch',height="content"):
    st.image('assets/banner.png')
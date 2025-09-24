import streamlit as st

st.title("Banner")

st.subheader("🌟 Concept")
st.write('''
         The banner serves as a visual introduction to attract attention and immediately convey the cultural identity of Shanghai.
         ''')
st.write ('''
          It captures the city’s essence through its iconic night view: a dark background with the moon sets the atmosphere, while bright contrasting tones highlight vibrancy. 
          Featuring the Bund’s four landmarks—the design guides the audience into Shanghai’s blend of tradition and modernity, making the banner both striking and memorable.
 
          ''')

st.subheader("🪧 Slogan")
st.write ('''
          - "more than just scenery": Highlights that the city offers more than what meets the eye—its history, lifestyle, and spirit go beyond the surface of visual beauty, inviting people to truly experience its essence.
          ''')

st.divider()



with st.container(width='stretch',height="content"):
    st.image('assets/banner.png')
import streamlit as st
st.title("Audio")
st.code('''
with st.container(width=800):
    st.audio('https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg',
             loop=True)''')

with st.container(width=800):
    st.audio('https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg',
             loop=True)

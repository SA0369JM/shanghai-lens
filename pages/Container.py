import streamlit as st
st.title("Layout")
st.code('''
with st.container(border=True,height=600,width=800):
    st.write('Inserts an invisible container into your app that can be used to hold multiple elements.')

''')

with st.container(border=True,height=600,width=800):
    st.write('Inserts an invisible container into your app that can be used to hold multiple elements.')

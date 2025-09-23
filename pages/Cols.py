import streamlit as st
st.title("Layout")
st.write('Streamlit provides several options for controlling how different elements are laid out on the screen.')
st.code('''
col1,col2,col3=st.columns([1,2,3],border=True,gap='small')
with col1:
    st.write('column1')
with col2:
    st.write('column2')
with col3:
    st.write('column3')

''')
col1,col2,col3=st.columns([1,2,3],border=True,gap='small')
with col1:
    st.write('column1')
with col2:
    st.write('column2')
with col3:
    st.write('column3')

import streamlit as st
st.title("Layout")

st.code('''
t1,t2,t3=st.tabs(['Tab1','Tab2','Tab3'])
with t1:
    st.write('Tab 1')
with t2:
    st.write('Tab 2')
with t3:
    st.write('Tab 3')

''')
t1,t2,t3=st.tabs(['Tab1','Tab2','Tab3'])
with t1:
    st.write('Tab 1')
with t2:
    st.write('Tab 2')
with t3:
    st.write('Tab 3')

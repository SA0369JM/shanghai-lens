
# pages/Poster.py
import streamlit as st
import time

st.set_page_config(page_title="Poster · Multimedia Container", page_icon="🖼️", layout="wide")
st.title('Storyboard')
st.code('''
row1 = st.columns(3)
row2 = st.columns(3)
for col in row1 + row2:
    tile = col.container(border=True)
    tile.image("assets/image_icon.png")
    tile.divider()
    tile.text("Lorem ipsum is placeholder text commonly used in the graphic," \
            "  print, and publishing industries for previewing layouts and visual mockups.")
    tile.divider()
''',wrap_lines=True)

row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
    tile = col.container(border=True)
    tile.image("assets/image_icon.png")
    tile.divider()
    tile.text("Lorem ipsum is placeholder text commonly used in the graphic," \
            "  print, and publishing industries for previewing layouts and visual mockups.")
    tile.divider()
    


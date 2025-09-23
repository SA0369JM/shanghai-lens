
# pages/1_Poster.py

import streamlit as st
st.write('You have to install `streamlit_image_coordinates` in your computer')

from streamlit_image_coordinates import streamlit_image_coordinates # type: ignore

st.code('''
def point_in_rect(x, y, rect, inclusive=True, tol=0.0):
    x1, y1, x2, y2 = rect
    left, right = sorted((x1, x2))
    top, bottom = sorted((y1, y2))
    if inclusive:
        return (left - tol <= x <= right + tol) and (top - tol <= y <= bottom + tol)
    else:
        return (left - tol <  x <  right + tol) and (top - tol <  y <  bottom + tol)
    
coords = streamlit_image_coordinates("assets/jaws.jpg",width=400)
if coords:
    if point_in_rect(coords['x'],coords['y'],(200,300,400,500)):
        st.switch_page('pages/2_Video.py')
    else:
        st.write('Not in the rect')
        ''')
def point_in_rect(x, y, rect, inclusive=True, tol=0.0):
    x1, y1, x2, y2 = rect
    left, right = sorted((x1, x2))
    top, bottom = sorted((y1, y2))
    if inclusive:
        return (left - tol <= x <= right + tol) and (top - tol <= y <= bottom + tol)
    else:
        return (left - tol <  x <  right + tol) and (top - tol <  y <  bottom + tol)
    
st.set_page_config(page_title="Poster · Multimedia Container", page_icon="🖼️", layout="wide")

coords = streamlit_image_coordinates("assets/jaws.jpg",width=400)
if coords:
    if point_in_rect(coords['x'],coords['y'],(200,300,400,500)):
        st.switch_page('pages/2_Video.py')
    else:
        st.write('Not in the rect')





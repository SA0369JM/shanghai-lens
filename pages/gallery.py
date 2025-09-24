
# pages/1_Poster.py
import streamlit as st
import time

st.title("Gallery")

st.write("Coming Soon with Shanghai Photo Gallery")
st.image('assets/comming_soon.png')

# # Your images: local paths or URLs
# IMAGES = [
#     "https://picsum.photos/seed/1/1200/700",
#     "https://picsum.photos/seed/2/1200/700",
#     "https://picsum.photos/seed/3/1200/700",
#     "https://picsum.photos/seed/4/1200/700",
# ]

# if "car_idx" not in st.session_state:
#     st.session_state.car_idx = 0

# #callback
# def shift(delta: int):
#     n = len(IMAGES)
#     st.session_state.car_idx = (st.session_state.car_idx + delta) % n

# l, mid, r = st.columns([1, 6, 1], gap="small")
# with l:
#     st.button("⟵", on_click=shift, args=[-1])
# with mid:
#     st.image(IMAGES[st.session_state.car_idx])
#     st.caption(f"{st.session_state.car_idx+1} / {len(IMAGES)}")
# with r:
#     st.button("⟶", on_click=shift, args=[1])


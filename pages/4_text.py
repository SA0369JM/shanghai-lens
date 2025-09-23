import streamlit as st

st.set_page_config(page_title="Streamlit Text Elements Showcase", layout="centered")

st.title("Streamlit Text Elements Showcase")
tabs = st.tabs([
    "Basics",
    "Markdown",
    "Badges",
])

with tabs[0]:
    with st.echo():
        st.title("This is `st.title()` (largest)",anchor='big_title')
        st.header("This is `st.header()` (medium)",\
                help='tips of my project',\
                divider='red')
        st.subheader("This is `st.subheader()` (small)")
        st.caption("This is a small, muted caption (good for footnotes).")
        st.divider()


with tabs[1]:
    st.header("Markdown")
    md = """
# H1 Heading (Markdown)
## H2 Heading
### H3 Heading

**Bold**, *italic*, ~~strikethrough~~, and `inline code`.

- Bullet list item 1
- Bullet list item 2
  - Nested item

1. Ordered item A
2. Ordered item B

> Blockquote: Markdown is great for rich formatting.

**Table**  
| Name | Type | Notes |
|------|------|-------|
| `st.markdown` | function | Renders Markdown |
| `st.write` | function | Renders many types |


Horizontal rule (Markdown):  
---
"""
    st.markdown(md)
    with st.expander("Show Markdown source"):
        st.code(md, language="markdown")

with tabs[2]:
    with st.echo():
        st.header("Badges")
        st.caption("Badges quickly spotlight key status or type information (e.g., NEW, Video), enabling fast scanning and comprehension without reading detailed text.")
        st.badge("COMP4415/ 5415")
        st.badge("Multimedia",color='orange')
        st.badge("Streamlit", icon=":material/check:", color="green")



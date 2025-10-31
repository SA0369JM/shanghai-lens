from __future__ import annotations
from pathlib import Path
from uuid import uuid4
import datetime as dt
import json
from PIL import Image, ImageSequence  # pip install pillow
import streamlit as st

st.set_page_config(page_title="Gallery", layout="wide")
st.title("Gallery")

# -------------------------
# Display sizes (tweak here)
# -------------------------
TOP_IMAGE_WIDTH = 640       # centered top photo width (px)
GALLERY_THUMB_WIDTH = 360   # review gallery thumbnail width (px)

# -------------------------
# Paths & constants
# -------------------------
ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
UPLOAD_DIR = ASSETS / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

PHOTOS_JSON  = ASSETS / "photos.json"   # list[str] of absolute image paths
REVIEWS_JSON = ASSETS / "reviews.json"  # list[dict]
ALLOWED_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff", ".gif"}

# -------------------------
# Persistence helpers
# -------------------------
def load_photos() -> list[str]:
    if PHOTOS_JSON.exists():
        try:
            data = json.loads(PHOTOS_JSON.read_text(encoding="utf-8"))
            return [p for p in data if Path(p).exists()]
        except Exception:
            return []
    return []

def save_photos(paths: list[str]) -> None:
    PHOTOS_JSON.write_text(json.dumps(paths, ensure_ascii=False, indent=2), encoding="utf-8")

def load_reviews() -> list[dict]:
    if REVIEWS_JSON.exists():
        try:
            return json.loads(REVIEWS_JSON.read_text(encoding="utf-8"))
        except Exception:
            return []
    return []

def save_reviews(items: list[dict]) -> None:
    REVIEWS_JSON.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")

def add_review(name: str, text: str, image_path: str) -> None:
    items = load_reviews()
    items.append(
        {
            "id": f"rvw-{uuid4().hex[:8]}",
            "name": name,
            "text": text,
            "image_path": image_path,
            "ts": dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    )
    save_reviews(items)

def delete_review(rid: str) -> None:
    items = load_reviews()
    items = [x for x in items if x.get("id") != rid]
    save_reviews(items)

# -------------------------
# Session state (restore library on first load)
# -------------------------
if "photos" not in st.session_state:
    st.session_state.photos: list[str] = load_photos()
if "photo_idx" not in st.session_state:
    st.session_state.photo_idx = max(len(st.session_state.photos) - 1, 0)
if "show_upload" not in st.session_state:
    st.session_state.show_upload = False
if "show_review_form" not in st.session_state:
    st.session_state.show_review_form = False

def current_image_path() -> str | None:
    if not st.session_state.photos:
        return None
    return st.session_state.photos[st.session_state.photo_idx]

def shift_photo(delta: int):
    n = len(st.session_state.photos)
    if n == 0:
        return
    st.session_state.photo_idx = (st.session_state.photo_idx + delta) % n

# -------------------------
# Top: centered photo area (smaller width)
# -------------------------
cur = current_image_path()
left_pad, mid, right_pad = st.columns([1, 2, 1])  # center column
with mid:
    if not cur:
        st.info("No image yet. Click **Upload** below to add one.")
    else:
        try:
            img = Image.open(cur)
            first = next(ImageSequence.Iterator(img))  # first frame only
            st.image(first, width=TOP_IMAGE_WIDTH)
            st.markdown(
                f"<div style='text-align:center;color:#6c757d;'>"
                f"{st.session_state.photo_idx + 1} / {len(st.session_state.photos)}</div>",
                unsafe_allow_html=True,
            )
        except Exception as e:
            st.error(f"Failed to open image: {e}")

# arrow controls (kept simple; disabled if <2 photos)
l, _, r = st.columns([1, 10, 1], gap="small")
with l:
    st.button("←", on_click=shift_photo, args=[-1], use_container_width=True,
              disabled=len(st.session_state.photos) < 2)
with r:
    st.button("→", on_click=shift_photo, args=[1], use_container_width=True,
              disabled=len(st.session_state.photos) < 2)

st.divider()

# -------------------------
# Actions: Upload | Review | Save photo to Gallery
# -------------------------
b1, b2, b3 = st.columns([1, 1, 1])
with b1:
    if st.button("Upload", use_container_width=True):
        st.session_state.show_upload = True
        st.session_state.show_review_form = False
with b2:
    if st.button("Review", use_container_width=True):
        st.session_state.show_review_form = True
        st.session_state.show_upload = False
with b3:
    if st.button("Save photo to Gallery", use_container_width=True):
        p = current_image_path()
        if not p:
            st.warning("Please upload an image first.")
        else:
            add_review(name="(Photo)", text="", image_path=p)
            st.success("Photo saved to Review Gallery.")
            st.rerun()

# Upload control (single file, append to library)
if st.session_state.show_upload:
    file = st.file_uploader(
        "Select ONE image",
        type=[e.strip(".") for e in ALLOWED_EXTS],
        accept_multiple_files=False,
        help="Every upload is added to your library (older photos stay).",
    )
    if file is not None:
        ext = Path(file.name).suffix.lower()
        if ext not in ALLOWED_EXTS:
            st.warning("Unsupported file type.")
        else:
            fname = f"{dt.datetime.now().strftime('%Y%m%d-%H%M%S')}-{uuid4().hex[:6]}{ext}"
            out_path = UPLOAD_DIR / fname
            out_path.write_bytes(file.getbuffer())

            st.session_state.photos.append(str(out_path))
            save_photos(st.session_state.photos)
            st.session_state.photo_idx = len(st.session_state.photos) - 1

            st.success("Image uploaded and added to your library.")
            st.session_state.show_upload = False
            st.rerun()

# Review form (for CURRENT photo)
if st.session_state.show_review_form:
    st.subheader("Write a Review")
    p = current_image_path()
    if not p:
        st.warning("Please upload an image first.")
    else:
        with st.form("review_form", clear_on_submit=True):
            name = st.text_input("Name (optional)", value="")
            review_text = st.text_area("Review", placeholder="Type your review here...", height=120)
            submitted = st.form_submit_button("Submit")
            if submitted:
                if not review_text.strip():
                    st.warning("Review cannot be empty.")
                else:
                    add_review((name or "Anonymous").strip(), review_text.strip(), p)
                    st.success("Review saved to Gallery.")
                    st.session_state.show_review_form = False
                    st.rerun()

st.divider()

# -------------------------
# Bottom: Review Gallery (deletable)
# -------------------------
st.subheader("📚 Review Gallery")
items = load_reviews()
if not items:
    st.info("No reviews yet. Upload a photo and submit your first review.")
else:
    for it in reversed(items):
        c_img, c_text, c_actions = st.columns([2, 3, 1], vertical_alignment="top")
        with c_img:
            p = Path(it["image_path"])
            if p.exists():
                try:
                    img = Image.open(p)
                    first = next(ImageSequence.Iterator(img))
                    st.image(first, width=GALLERY_THUMB_WIDTH)
                except Exception as e:
                    st.warning(f"Cannot open image: {e}")
            else:
                st.warning("Image file not found on disk.")
        with c_text:
            display_name = it.get("name") or "Anonymous"
            st.markdown(f"**{display_name}** · *{it.get('ts','')}*")
            txt = it.get("text", "")
            if txt:
                st.write(txt)
            else:
                st.caption("No review text (photo entry).")
        with c_actions:
            if st.button("Delete", key=f"del-{it['id']}", type="secondary"):
                delete_review(it["id"])
                st.toast("Deleted.", icon="🗑️")
                st.rerun()
        st.markdown("---")

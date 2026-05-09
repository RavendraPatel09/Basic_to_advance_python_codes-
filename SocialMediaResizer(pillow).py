import streamlit as st
from PIL import Image, ImageOps
import io
st.title("Simple Photo Resizer")
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png"])
if uploaded_file is not None:
    photo = Image.open(uploaded_file)
    st.image(photo, caption="Original")
    st.write("### Resized Versions")
    insta_img = ImageOps.fit(photo, (1080, 1080))
    st.image(insta_img, caption="Instagram Square")
    link_img = ImageOps.fit(photo, (1200, 627))
    st.image(link_img, caption="LinkedIn Landscape")
    twit_img = ImageOps.fit(photo, (1600, 900))
    st.image(twit_img, caption="Twitter Header")
    buf = io.BytesIO()
    insta_img.convert("RGB").save(buf, format="JPEG")
    st.download_button("Download Instagram Photo", data=buf.getvalue(), file_name="insta.jpg")
print("Thankyou for using ")
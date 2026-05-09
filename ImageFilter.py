from PIL import Image, ImageFilter
import streamlit as st  
st.title("Image Filter")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
filter_type = st.selectbox("Select Filter Type", ["Original", "Blur", "Sharpen", "Edge Enhance","GrayScale","contour"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    if filter_type == "Blur":
        filtered_image = image.filter(ImageFilter.BLUR)
    elif filter_type == "Sharpen":
        filtered_image = image.filter(ImageFilter.SHARPEN)
    elif filter_type == "Edge Enhance":
        filtered_image = image.filter(ImageFilter.EDGE_ENHANCE)
    elif filter_type == "GrayScale":
        filtered_image = image.convert("L")
    elif filter_type == "contour":
        filtered_image = image.filter(ImageFilter.CONTOUR)
    else:
        filtered_image = image
    st.image(filtered_image, caption='Filtered Image', use_column_width=True)


    
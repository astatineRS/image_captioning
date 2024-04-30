import ImageCaption
import streamlit as st
from PIL import Image
import os


def caption_image(image):
    caption = ImageCaption.caption_this_image(image)
        
    result_dic = {
            'image' : image,
            'caption' : caption
        }
    return result_dic

st.title("Image Captioning")

uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image_path = os.path.join("./temp", uploaded_image.name)
    with open(image_path, "wb") as f:
        f.write(uploaded_image.read())

    image = Image.open(image_path)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    if st.button("Caption Image"):
        caption = caption_image(image_path)    
        st.write(caption["caption"])


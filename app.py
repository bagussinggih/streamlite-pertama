
import streamlit as st
from PIL import Image, ImageEnhance
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Menambahkan judul
st.title("Aplikasi Manipulasi Gambar")

# Upload gambar
uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Membuka gambar
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    # Menampilkan gambar asli
    st.image(image, caption='Gambar Asli', use_column_width=True)

    # RGB ke HSV
    hsv_image = cv2.cvtColor(img_array, cv2.COLOR_RGB2HSV)
    st.image(hsv_image, caption='Gambar dalam HSV', use_column_width=True, channels="HSV")

    # Histogram
    st.subheader('Histogram')
    fig, ax = plt.subplots()
    color = ('r', 'g', 'b')
    for i, col in enumerate(color):
        histr = cv2.calcHist([img_array], [i], None, [256], [0, 256])
        ax.plot(histr, color=col)
        ax.set_xlim([0, 256])
    st.pyplot(fig)

    # Brightness dan Contrast
    brightness = st.slider('Atur Kecerahan', 0.0, 2.0, 1.0)
    contrast = st.slider('Atur Kontras', 0.0, 2.0, 1.0)
    enhancer = ImageEnhance.Brightness(image)
    image_brightened = enhancer.enhance(brightness)
import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import h5py as h5
from tensorflow.keras.models import load_model
import subprocess
import os

if not os.path.isfile('model.h5'):
    subprocess.run(['curl --output model.h5 "https://media.githubusercontent.com/media/MuhammadAqhariNasrin/Optimizing-Solar-Panel-Efficiency-Computer-Vision-Approach-to-Dust-Detection-on-Solar-Panel/main/solarpanelimageclassifier.h5"'], shell=True)


model = tf.keras.models.load_model('model.h5',compile=False)

# Streamlit app
st.title("Solar Panel Classifier")

# Display information about the author and data source
st.subheader("About the Author:")
st.text("Name: Muhammad Aqhari Nasrin")
st.text("Email: muhammad.aqhari.nasrin@gmail.com")
st.markdown("LinkedIn: [Muhammad Aqhari Nasrin](https://www.linkedin.com/in/muhammad-aqhari-nasrin)")

# Upload image through Streamlit interface
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Function to make predictions
def make_prediction(image):
    resize = tf.image.resize(image, (256, 256))
    yhat = model.predict(np.expand_dims(resize/255, 0))
    return yhat[0][0]

# Display results
if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Read the image using PIL
    img = Image.open(uploaded_file)

    # Convert the image to a numpy array
    img_array = np.array(img)

    # Make prediction
    prediction = make_prediction(img_array)

    # Display the results
    if prediction > 0.5:
        st.write("Prediction: Dusty Solar Panel")
    else:
        st.write("Prediction: Clean Solar Panel")

st.markdown("[Download Sample Data](https://drive.google.com/drive/folders/12Q3MBI8SPw0vHsO_kkS5izkxw0F7tXx4)")


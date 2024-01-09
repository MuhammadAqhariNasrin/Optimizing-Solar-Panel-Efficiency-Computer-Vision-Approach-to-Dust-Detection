import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load your trained model
model = tf.keras.models.load_model(r"C:\Users\muham\OneDrive\Desktop\Solar Panel Computer Vision\dataset\Model\solarpanelimageclassifier.h5")

# Streamlit app
st.title("Solar Panel Classifier")

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

import streamlit as st
from predictions import make_prediction
from image_preprocessor import preprocess_image

# Title of the app
st.title("Potato Disease Classification")

# File uploader for the user to upload images
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # Preprocess the uploaded image
        image = preprocess_image(uploaded_file)  # Pass the UploadedFile object directly
        st.write("Image preprocessing complete.")

        # Make prediction
        label, confidence = make_prediction(image)  # Ensure make_prediction handles the preprocessed image
        st.write("Prediction complete.")

        # Display the results
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        st.write(f"Prediction: {label} with confidence {confidence:.2f}")
    except Exception as e:
        st.error(f"Error: {e}")
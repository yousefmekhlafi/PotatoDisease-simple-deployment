import os
from keras.models import load_model  # or from tensorflow.keras.models import load_model if using TensorFlow's Keras

# Define the model path
model_path = 'model/potatoes.h5'  # Use relative path or absolute path

# Check if the model file exists
if os.path.exists(model_path):
    print(f"Model file found at {model_path}")
    # Optionally load the model to test if it works
    model = load_model(model_path)
    print("Model loaded successfully.")
else:
    print(f"Model file not found at {model_path}")
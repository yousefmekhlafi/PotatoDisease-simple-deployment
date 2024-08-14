import os
import numpy as np
import tensorflow as tf
from keras.models import load_model

# Load the pre-trained model
model_path = os.path.join('model', 'potatoes.h5')
model = load_model(model_path)

# Define the class labels
class_labels = ['Early Blight', 'Late Blight' , 'Healthy']

def make_prediction(img_array):
    """
    Predict the class of the given image.

    Parameters:
    - img_array: Preprocessed image array.

    Returns:
    - label: Predicted class label.
    - confidence: Confidence score of the prediction.
    """
    # Make the prediction
    predictions = model.predict(img_array)
    
    # Get the predicted class index
    predicted_class = np.argmax(predictions)

    # Get the label and confidence score
    label = class_labels[predicted_class]
    confidence = predictions[0][predicted_class]

    return label, confidence
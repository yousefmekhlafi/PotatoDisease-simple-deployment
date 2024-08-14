from keras_preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import io

def preprocess_image(uploaded_file, target_size=(256, 256)):
    """
    Preprocesses the uploaded image for model prediction.

    Parameters:
    - uploaded_file: Streamlit UploadedFile object
    - target_size: Tuple specifying the target size for the image

    Returns:
    - img_array: Preprocessed image array ready for prediction
    """
    # Convert the UploadedFile to a PIL Image object directly
    image_data = io.BytesIO(uploaded_file.read())
    img = Image.open(image_data)

    # Resize the image to the target size
    img = img.resize(target_size)

    # Convert the image to a numpy array
    img_array = img_to_array(img)

    # Normalize the image array (pixel values to range [0, 1])
    img_array = img_array / 255.0

    # Expand dimensions to match the model's expected input shape
    img_array = np.expand_dims(img_array, axis=0)

    return img_array
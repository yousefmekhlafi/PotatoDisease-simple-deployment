# Potato Leaf Disease Classification (Simple Deployment)

App status: FUNCTIONAL: tested on postman and streamlit

# Description

This is a deep learning classification app for detecting a potato plant disease. The DL algorithm classifies potato leaves into 3 different classes: healthy, early blight, late blight.


# Disclaimers

The project's model was developed on a jupyter notebook externally with Codebasics YT Channel, but the packaging and deployment is personal effort

ChatGPT was thoroughly used for learning and assisting purposes. 

Project video: https://www.youtube.com/watch?v=2s-tmKc3gKw&list=PLPbgcxheSpE1gl5WkrwtmRiCwiGMM8NdH&index=3&pp=iAQB


# Project Scope and Goals

1. Learn Python
2. Learn deep learning
3. Learn computer vision
4. Learn how to process and work with image data
5. Learn how to deploy models in a simple workflow and web framework  


# How to Run

# Option 1: On your local machine 

1. Clone this repository and run on VS code
2. Create a virtual environment:

"git clone https://github.com/yousefmekhlafi/PotatoDisease-simple-deployment"

2. Activate virtual environment
"conda activate potato-simple-5"

3. install requirements.txt

"pip install -r requirements.txt"

4. type in command "streamlit run app.py" on terminal

Option 2: 
Use cloud services for containerization and deployment using your own resources



# Project Methodology  

1. Entirety of experiment and model training was done in a jupyter notebook first

Step 1: the image dataset was processed into a tensorflow dataset

Step 2: The data was augmented as well due to the limited size of the dataset

Step 3: The model was trained with a CNN and saved in .h5 format

Step 4: The model loss function and accuracy were plotted for overfitting detection

2. Created an image processing py file for processing input images for predictions

3. Created a predictions py file that loads the model and runs the prediction function on input data

4. Created a streamlit app for running these py in a simple drag/drop or upload-file UI

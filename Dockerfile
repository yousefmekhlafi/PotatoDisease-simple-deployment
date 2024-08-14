# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# working directory
WORKDIR /app

# copying requirements
COPY requirements.txt .

# installing dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copying application code 
COPY . .

# port exposing
EXPOSE 8501

# command for running app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
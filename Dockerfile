# Use the official Python image from Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Copy the .env file to the working directory
COPY .env /app/.env

# Install dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir --upgrade -r requirements.txt

# Expose the port that Streamlit will run on
EXPOSE 8501

# Command to run Streamlit when the container starts
CMD ["streamlit", "run", "app/app.py"]

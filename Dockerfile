# Use the official Python image from Docker Hub
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY app/requirements.txt /app/requirements.txt

# Copy the .env file into the container
COPY .env /app/.env

# Install system dependencies required for some packages
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the application code into the container
COPY app /app

# Expose the port that Streamlit will run on
EXPOSE 8501

# Command to run Streamlit when the container starts
CMD ["streamlit", "run", "app.py"]

# Use the official Python image from Docker Hub
FROM python:3.11-slim

# Install dnsutils
RUN apt-get update && apt-get install -y dnsutils

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY app/requirements.txt /app/requirements.txt

# Copy the .env file into the container
COPY .env /app/.env

# Copy the application code into the container
COPY app /app

# Install dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir --upgrade -r requirements.txt

# Expose the port that Streamlit will run on
EXPOSE 8501

# Command to run Streamlit when the container starts
CMD ["streamlit", "run", "app.py"]

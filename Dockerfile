# Use the official Python image from Docker Hub
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY app/requirements.txt /app/requirements.txt

# Copy the .env file into the container
COPY .env /app/.env



# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the application code into the container
COPY app /app

# Expose the port that Streamlit will run on
EXPOSE 8501

# Command to run Streamlit when the container starts
CMD ["streamlit", "run", "app.py"]

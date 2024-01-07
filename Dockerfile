# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y nano  # Install nano for debugging
RUN pip install --no-cache-dir -r requirements.txt
    
# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable for Django
ENV DJANGO_SETTINGS_MODULE=bnmc.settings

# Run app.py when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "bnmc.wsgi:application"]

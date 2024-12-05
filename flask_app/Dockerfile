# Use Python base image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY app/requirements.txt /app/requirements.txt

# Install dependencies, dont save in cache to make image smaller
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application folder into the container
COPY app /app

# Expose the port the app runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "main.py"]
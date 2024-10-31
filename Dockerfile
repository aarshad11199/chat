# Base image with Python
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Start the Flask app
CMD ["python", "server.py"]

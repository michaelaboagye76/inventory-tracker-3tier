# Use lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Nginx
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

# Copy Nginx config
COPY default.conf /etc/nginx/conf.d/default.conf

# Copy app code
COPY . .

# Expose port 80 (only one port used — compatible with ECS/Beanstalk)
EXPOSE 80

# Start Gunicorn (Flask app) and Nginx together
CMD service nginx start && gunicorn --bind 0.0.0.0:80 app:app


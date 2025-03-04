# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose port 5000 (Flask default)
EXPOSE 5000

# Start the app
CMD ["python3", "app.py"]


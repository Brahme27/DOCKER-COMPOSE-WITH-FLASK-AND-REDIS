# Use lightweight Python image
FROM python:3.7-alpine  

# Set working directory
WORKDIR /code    

# Copy and install dependencies
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt  

# Copy the app code
COPY . .  

# Expose port for Flask
EXPOSE 5000  

# Run the app
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]


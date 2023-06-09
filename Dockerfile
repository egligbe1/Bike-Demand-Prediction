# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container at /app
COPY . /app
#
## Set environment variables
#ENV FLASK_APP=app.py
#ENV FLASK_ENV=production

# Expose port 5000 for the Flask app to listen on
EXPOSE 5000

# Start the Flask app
CMD ["flask", "run", "--host", "0.0.0.0"]

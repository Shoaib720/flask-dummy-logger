# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install cron and logrotate
RUN apt-get update && apt-get install -y cron logrotate && rm -rf /var/lib/apt/lists/*
# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set up log rotation
COPY .docker/logrotate.conf /etc/logrotate.d/messages
RUN chmod 644 /etc/logrotate.d/messages

# Run the cron daemon in the background
RUN crontab -l | { cat; echo "* * * * * /usr/sbin/logrotate /etc/logrotate.d/messages"; } | crontab -

# Expose port 8000 for the Flask application
EXPOSE 8000

# Define the command to run your application with Gunicorn
# CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8000", "app:app"]
CMD ["sh", "-c", "cron && gunicorn --workers 4 --bind 0.0.0.0:8000 app:app"]
# CMD ["sh", "-c", "cron && python manage.py runserver 0.0.0.0:8000"]

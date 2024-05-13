# Use the official Python 3 base image
FROM python:3

# Set environment variables to disable writing bytecode and buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements.txt file to the container's working directory
COPY requirements.txt /code/

# Install Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code to the container's working directory
COPY . /code/

# Define the default command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
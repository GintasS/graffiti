# Set base image (host OS)
FROM python:3.7.12-buster

# Set timezone for Europe/Vilnius.
RUN cp /usr/share/zoneinfo/Europe/Vilnius /etc/localtime
RUN echo "Europe/Vilnius" > /etc/timezone

# By default, listen on port 8000
EXPOSE 8000/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
CMD [ "python", "./runserver.py" ]
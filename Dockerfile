FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

ENV API_KEY=${API_KEY}
ENV MAIL_USERNAME=${MAIL_USERNAME}
ENV MAIL_PASSWORD=${MAIL_PASSWORD}
ENV MAIL_FROM=${MAIL_FROM}
ENV MAIL_PORT=${MAIL_PORT}
ENV MAIL_SERVER=${MAIL_SERVER}


# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
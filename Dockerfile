FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /home/django/

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py makemigrations && python manage.py migrate
CMD ["/bin/sh", "start.sh"]
FROM python:3.7


ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .


#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:$PORT"]

#work just with dinamic content
#CMD ["sh", "-c", "gunicorn  app.wsgi:application --bind 0.0.0.0:8000"]

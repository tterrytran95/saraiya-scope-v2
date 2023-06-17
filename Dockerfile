FROM python:3.9

WORKDIR /usr/src/bioscope

COPY . /usr/src/bioscope 

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
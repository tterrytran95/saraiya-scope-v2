FROM python:3.9

WORKDIR /usr/src/bioscope

COPY . /usr/src/bioscope 

RUN pip install -r requirements.txt
RUN sh initialize.sh

# CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
EXPOSE 8000
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
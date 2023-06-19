FROM python:3.9

WORKDIR /usr/src/bioscope

COPY . /usr/src/bioscope 

RUN pip install -r requirements.txt
EXPOSE 8000
# RUN ["python", "manage.py", "runserver", "127.0.0.1:8000" ">", "frontend_output.log", "&"]
# RUN python3 manage.py runserver 127.0.0.1:8000 > frontend.log &
# RUN python3 saraiyascope/utils/image_utils.py
RUN sh initialize.sh

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
# CMD ["echo", "python3", "--version"]
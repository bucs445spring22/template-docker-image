FROM python:3.9-alpine

WORKDIR /var/app

#installs dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /var/tmp/requirements.txt
RUN pip install -r /var/tmp/requirements.txt

#copies the application files
COPY ./app.py /var/app/app.py

CMD ["python","-Werror","app.py"]

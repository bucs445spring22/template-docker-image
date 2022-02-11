FROM python:3.9-alpine

WORKDIR /var/app

#installs dependencies
RUN pip install --upgrade pip
COPY ./app/requirements.txt /var/tmp/requirements.txt
RUN pip install -r /var/tmp/requirements.txt

CMD ["ash"]
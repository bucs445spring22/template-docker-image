FROM python:3.9-alpine

WORKDIR /var/db

#installs dependencies
RUN pip install --upgrade pip
COPY ./db/requirements.txt /var/tmp/requirements.txt
RUN pip install -r /var/tmp/requirements.txt

CMD ["ash"]
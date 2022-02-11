# Containerized Python App Template

A template for a containerized python app

## Commands Cheatsheet

### Docker

#### Build

docker build -t image_name .

#### Run

docker run image_name
docker run -d -it --name app -p 80:5000 image_name

#### Volumes

docker run --rm -v "$(pwd)/app:/var/app docker-example"

### Docker Compose

docker-compose pull
docker-compose up --build -d
docker-compose down --remove-orphans

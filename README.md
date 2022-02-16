# Containerized Python App Template

A template for a containerized python app

## Commands Cheatsheet

### **Docker**

#### ***Build***

* *docker build -t `image_name` .*

#### ***Run***

* *docker run `image_name`*
* *docker run -d -it --name app -p 80:5000 `image_name`*

#### ***Attach***

* *docker attach `container_name`*

#### ***Volumes***

* docker run -v "$(pwd)/app:/var/app" docker-example
  * TODO: Details
* docker run -v "/var/app/lib" docker-example
  * TODO: Details
* docker run -v "$(pwd)/app:/var/app" -v "/var/app/lib" docker-example
  * TODO: Details

### ***Docker Compose***

* *docker-compose pull*
  * TODO: Details
* *docker-compose up --build -d*
  * TODO: Details
* *docker-compose down --remove-orphans*
  * TODO: Details

## Debugging a Container:

1. Check the logs
    * docker logs [OPTIONS] CONTAINER
2. Run the container separately in interactive mode and attach
3. One the container is running, you can use the below command to get access to a container rif it was put in the background:
        * `db attach CONTAINER`
        * *Keep in mind that you are attaching to the current running process not the system, so if it is not an interactive process (like a web server instead of a shell), then you will just get a blank screen. When you exit the interactive shell, you will also be exiting the process, shutting down the container*

***Helpful Hints***
    * When debugging a system level issue, change the CMD to the shell,

```python 
    some_shells =  {"bash":"sh", "alpine":"ash", "Korn shell":"ksh"}
```

Then run things manually by attaching tot he container

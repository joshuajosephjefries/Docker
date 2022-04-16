<!DOCTYPE html>
<html>
     <body>
       <h1> DOCKER COMPOSE </h1>
       <p>
         Docker Compose is a tool for running multi-container applications on Docker defined using the Compose file format. 
         A Compose file is used to define how the one or more containers that make up your application are configured. 
         Once you have a Compose file, you can create and start your application with a single command: "docker compose up".
       </p>
       <h1> PROJECT OVERWIEW </h1>
       <h2> Aim </h2>
       <p>
         The main goal of this project is to create a website with Docker Compose, Flask framework and Redis to maintain hit count of the website.
       </p>
       <h2> Project Requirements </h2>
       <p>
         1. Install docker 
            yum install docker -> Installation of docker
            docker --version -> Checking the docker version
         2. Docker compose -(https://docs.docker.com/compose/install/#alternative-install-options)
            pip3 install docker-compose -> Installing docker-compose
            chmod +x /usr/local/bin/docker-compose -> Adding permissions to the file called docker-compose
            ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose -> Link the path name
            docker-compose --version -> Check the docker-compose version
         3. Python -> Defaultly installed on all linux machines
         4. Redis -> Open source that is a database for in-memory data structure storage
       </p>
    </body>
</html>          

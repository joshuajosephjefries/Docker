<!DOCTYPE html>
<html>
     <body>
          <h1>DOCKER</h1>
          <h2> Dockerfile 1 </h2> 
          <p>  
               Dockerfile to create a git image
               <br> To build an image: "docker build -t gitimage ."
               <br> To make/run/attach/execute a container: "docker run -it gitimage /bin/bash"
               <br> To exit the container: Ctrl P Q
               <br> Do not force exit the container as it goes into the exited mode. 
               <br> Everytime a line/instruction is run, docker discards intermediate container. 
               <br> Therefore, tail -f /dev/null does not make the container go into exited mode.
          </p>
          <hr>
          <h2> Dockerfile 2 </h2>
          <p> 
               Dockerfile to create ansible image
               <br> To build, run "docker build -t ansibleimage ."
               <br> To make/run/attach/execute a container: "docker run -it ansibleimage /bin/bash"
               <br> To exit the container: Ctrl P Q
               <br> Do not force exit the container as it goes into the exited mode.
               <br> Everytime a line/instruction is run, docker discards intermediate container. 
               <br> Therefore, tail -f /dev/null does not make the container go into exited mode.
          </p>
          <hr>
          <h2> Dockerfile 3 </h2>
          <p>
               Dockerfile to create a new volume using VOLUME instruction
               <br> To build an image: "docker build -t volumeimage ."
               <br> To make/run/attach/execute a container: "docker run -it volumeimage /bin/bash"
               <br> To exit the container: Ctrl P Q
               <br> Do not force exit the container as it goes into the exited mode. 
               <br> Everytime a line/instruction is run, docker discards intermediate container. 
               <br> Therefore, tail -f /dev/null does not make the container go into exited mode.
          </p>
          <hr>
          <h2> Dockerfile 4 </h2>
          <p>
               Dockerfile to build an image that contains apache2 webserver and create a html file to display on website
               <br> To build an image: "docker build -t webserver ."
               <br> To make/run/attach/execute a container: "docker run -it --name webcontainer -p 8080:80 webserver /bin/bash"
               <br> Check the status of apache2: "systemctl status apache2.service" && "systemctl start apache2.service"
               <br> To exit the container: Ctrl P Q
               <br> Do not force exit the container as it goes into the exited mode. 
               <br> Everytime a line/instruction is run, docker discards intermediate container. 
               <br> Therefore, tail -f /dev/null does not make the container go into exited mode.
               <br> To access container on web: Private_IP_Address: Port number (8080)
          </p>
          <hr>
          <h2> Dockerfile 5 </h2>
          <p>  
               Dockerfile to install jenkins along with jenkins CLI
               <br> To build an image: "docker build -t myjenkins-blueocean:2.332.2-1 ."
               <br> To make/run/attach/execute a container: "docker run --name jenkins-blueocean --rm --detach --network jenkins --env DOCKER_HOST=tcp://docker:2376                  <br> --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 --publish 8080:8080 --publish 50000:50000 --volume jenkins-data:/var/jenkins_home                  <br> --volume jenkins-docker-certs:/certs/client:ro myjenkins-blueocean:2.332.2-1"
               <br> To exit the container: Ctrl P Q
               <br> Do not force exit the container as it goes into the exited mode. 
          </p>
          <hr>
          <h2> How to create a docker inside docker </h2>
          <p>
               <img width="638" alt="Docker_inside_docker" src="https://user-images.githubusercontent.com/79646955/165822648-9d5f592b-82ee-4739-a376-ce4bb10e827c.png" style="vertical-align:middle">
          </p>
          </hr>
     </body>
</html>
 

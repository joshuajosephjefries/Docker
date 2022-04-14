<!DOCTYPE html>
<html>
     <body>
          <h1>DOCKER</h1>
          <h2> Dockerfile 1 </h2> 
          <p>  
               Dockerfile to create a git image
               To build an image: "docker build -t gitimage ."
               To make/run/attach/execute a container: "docker run -it gitimage /bin/bash"
               To exit the container: Ctrl P Q
               Do not force exit the container as it goes into the exited mode. 
               Everytime a line/instruction is run, docker discards intermediate container. 
               Therefore, tail -f /dev/null does not make the container go into exited mode.
          </p>
          <hr>
          <h2> Dockerfile 2 </h2>
          <p> 
               Dockerfile to create ansible image
               To build, run "docker build -t ansibleimage ."
               To make/run/attach/execute a container: "docker run -it ansibleimage /bin/bash"
               To exit the container: Ctrl P Q
               Do not force exit the container as it goes into the exited mode.
               Everytime a line/instruction is run, docker discards intermediate container. 
               Therefore, tail -f /dev/null does not make the container go into exited mode.
          </p>
          <hr>
          <h2> Dockerfile 3 </h2>
          <p>
               Dockerfile to create a new volume using VOLUME instruction
               To build an image: "docker build -t volumeimage ."
               To make/run/attach/execute a container: "docker run -it volumeimage /bin/bash"
               To exit the container: Ctrl P Q
               Do not force exit the container as it goes into the exited mode. 
               Everytime a line/instruction is run, docker discards intermediate container. 
               Therefore, tail -f /dev/null does not make the container go into exited mode.
          </p>
          <hr>
          <h2> Dockerfile 4 </h2>
          <p>
               Dockerfile to build an image that contains apache2 webserver and create a html file to display on website
               To build an image: "docker build -t webserver ."
               To make/run/attach/execute a container: "docker run -it --name webcontainer -p 8080:80 webserver /bin/bash"
               Check the status of apache2: "systemctl status apache2.service" && "systemctl start apache2.service"
               To exit the container: Ctrl P Q
               Do not force exit the container as it goes into the exited mode. 
               Everytime a line/instruction is run, docker discards intermediate container. 
               Therefore, tail -f /dev/null does not make the container go into exited mode.
               To access container on web: Private_IP_Address: Port number (8080)
          </p>
          <hr>
     </body>
</html>
 

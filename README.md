# Docker
# This repository consists of DOCKERFILES that are used to install applications or instances

<h1> Dockerfile 1 </h1> 
<p>  Dockerfile to create a git image
     To build an image: "docker build -t gitimage ."
     To make/run/attach/execute a container: "docker run -it gitimage /bin/bash"
     To exit the container: Ctrl P Q
     Do not force exit the container as it goes into the exited mode. 
     Everytime a line/instruction is run, docker discards intermediate container. 
     Therefore, tail -f /dev/null does not make the container go into exited mode.
  </p>
 

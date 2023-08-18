# Docker Exam
1. What command(s) do you use to run MariaDB in Docker on your machine and map its port to the port 12345 on your machine? 
It should contain a database called prework.
```
docker run --detach --rm \
    --name imc-mariadb \
    --network imc --network-alias mariadb \
    -v imc:/var/lib/mysql \
    -e MARIADB_USER=kevin \
    -e MARIADB_PASSWORD=123 \
    -e MARIADB_ROOT_PASSWORD=123 \
    -e MARIADB_DATABASE=prework \
    -p 12345:3306  \
    mariadb:latest
```

2. What command(s) do you use on your local machine to open a prompt into the MariaDB server from step 1? You can use any Mysql client.
```
docker exec -it imc-mariadb bash
mariadb -D prework -u root -p
```

3. Clone https://github.com/imc-trading/devschool-docker-exam

4. How do you run step 1 but use init.sql to initialize the database?
```
use bind mount to mount host dir where the init script is to the dir used by MariaDB to execute initialisation scripts during container startup.

docker run --detach --rm \
    --name imc-mariadb \
    --network imc --network-alias mariadb \
    -v imc:/var/lib/mysql \
    --mount type=bind,src="/Users/kevin/PycharmProjects/imc_dev_python_prework/docker",target=/docker-entrypoint-initdb.d \
    -e MARIADB_USER=kevin \
    -e MARIADB_PASSWORD=ftw \
    -e MARIADB_ROOT_PASSWORD=ftw \
    -e MARIADB_DATABASE=prework \
    -p 12345:3306  \
    mariadb:latest
```

5. What command do you use to open bash console in your running MariaDB container?
```
docker exec -it imc-maria bash
```

6. What commands do you use to list containers, list images, stop a container, start a container, remove a container?
```
list containers: docker container ls
list images: docker image ls
stop a container: docker container stop [id]
start a container: docker container start [id] 
remove a container: docker rm [id]

```

7. In server.py you have a small Python server implementation. 
Please create a custom Docker image around it and a Docker compose that starts up this server and the MariaDB container from the steps above. 
The server should connect to the MariaDB container and it should expose its HTTP port to localhost’s port 8082. 
How do you check that the server works? Note that the server has requirements that must be installed with pip install -r requirements.txt
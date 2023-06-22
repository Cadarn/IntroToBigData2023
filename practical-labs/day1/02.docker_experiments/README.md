# Docker Experiments

We spent a significant chunk of Day 1 of the workshop introducting Docker as a technology that is useful in its own right but is also crucial to the rest of the workshop. The order of the practical labs session is as follows:
1. Read through the DockerQuickstart document
2. Use Docker to start a mongo database and use the 03-DockerExperiments.ipynb to interact with it and play.
3. Go to the `docker_python` folder.
    - In this folder we have a `Dockerfile` that you can build and run to create a JupyterLab environment inside of a container. You can build the image using: `docker build -t jupyter-dock .`
4. Still in the `docker_python` folder I completed the docker-compose example that didn't work during the workshop. Please inspect the `docker-compose.yaml` file to see what it contains and then do the following:
    - `docker compose build`
    - `docker compose up`
    - In a web browser go to `localhost:8888` - make sure you aren't still running your own Jupyter lab that is using this port. The password to login is `datarocks`
    - In the Jupyter Lab environment you should see a single notebook that you can run to interact with a PostgreSQL database that was launched as part of the Docker compose file.

Also in the folder are two extra resources:
- A docker cheatsheet from the makers of Docker
- Another example of a Docker application which is more complicated and involved
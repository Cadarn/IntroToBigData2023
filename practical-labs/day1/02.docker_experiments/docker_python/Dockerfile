FROM continuumio/anaconda3:latest

# Install build-essentials to facilitate installation of Python dependencies
RUN apt-get update --fix-missing && apt-get install -y build-essential
RUN apt-get install -y git postgresql-client

WORKDIR /code/

COPY myenv.yml /code/.

RUN conda install nb_conda_kernels 
RUN conda env create -f myenv.yml 

EXPOSE 8888

# Copy Jupyter launch script
COPY launch.py /code/
COPY 03b-DockerComposeExperiments-Python_and_SQL.ipynb /code/.

ENTRYPOINT [ "/bin/bash" ]
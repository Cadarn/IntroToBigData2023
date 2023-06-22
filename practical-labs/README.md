# Practical Labs

The order of materials follows the order of the topics that covered in the lectures. To make them a little easier to navigate they are layed out by the day of the workshop in which they were given. The materials are best understood when combined with the workshop recordings which should have been made available separately. In summary we have:
1. day1
    - 01.jupyterlab_notebooks folder; these are the notebooks that incorporate our experiments in the Jupyter Lab environment.
    - 02.docker_experiments folder; here are a number of files, folders and notebooks that demonstrate how we experimented with using Docker to host and run different technologies and apps
2. day2
    - 03.local_spark_experiments folder; these are the materials we used to setup our local Spark cluster and begin experimenting with the Word Count mapr/reduce algorithm
    - 04.databricks_spark_experiments folder; these are the materials that support moving into the Databricks cloud for running Spark jobs.
    - 05.sql_experiments folder; there is a notebook and a notebook solution that demonstrated using DuckDB as an in-memory SQL database. The objective was to showcase a little bit of SQL; how to get started with SQL in Python; showcasing the speedup that DuckDB can deliver.
3. day3
    - 06.rabbitmq_experiments folder; these are the problems and solutions that we worked on using RabbitMQ as an example message broker service.
    - 07.prefect_experiments folder; these are a couple of very, basic python scripts that illustrate how to get started with Prefect.
    - 08.streamlit_experiemnts folder; within this folder are two examples of apps that we built live in the workshop to showcase how to build interactive data dashboards/apps with the Streamlit framework

    Within the root directory there is the `IBD23-workshop.yml` file - this file can be used with an Anaconda installation to build an environment that should have all the libraries and tools to run these practical assignments. It can be installed with:
    
    ```
    conda env create -f IBD23-workshop.yml
    ```

    Note you will also need Docker installed and to pull the images required by each assignment.
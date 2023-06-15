from prefect import flow, task
import requests


@task
def say_hello():
	msg = "Hello, World! I'm Marvin!"
	print(msg)
	return msg


@flow()
def marvin_flow():
	msg = say_hello()
	

if __name__ == "__main__":
    marvin_flow() # "Hello, World! I'm Marvin!"
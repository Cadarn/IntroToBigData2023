#!/usr//bin/python
import pika
import sys, os
import numpy as np
import time

def main():

    # Setup RabbitMQ connection
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))


    # Write your code here

    print(f" ALL MESSAGES SENT")
    connection.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

#!/usr/bin/python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# Code here

connection.close()

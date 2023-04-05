#!/usr/bin/env python
import pika
import sys
import numpy as np

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message_list = [
    "Greetings and salutations",
    "I \u2665 Python",
    "Big Data is Awesome",
    "I used Apache Spark yesterday"
]

for i in range(int(sys.argv[1])):
    if i%2 == 0:
        delay = np.random.randint(5,12)
    else:
        delay = np.random.randint(1,7)

    dots = "."*delay
    message = f"{i+1} - {np.random.choice(message_list)} {dots}"

    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    print(" [x] Sent %r" % message)



connection.close()

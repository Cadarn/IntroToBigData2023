#!/usr//bin/python
import pika
import sys, os
import numpy as np
import time

def main():

    # Setup RabbitMQ connection
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    # Setup out messages
    message_selection = [
    "Hello friend",
    "Live long and prosper",
    "Yo dude!",
    "Alright",
    "Ciao",
    "Greetings, ladies and gentlemen."
    ]

    number_of_messages_to_send = 100

    for timedelay in np.random.uniform(low=0.1, high=2.0, size=number_of_messages_to_send):
        time.sleep(timedelay)

        chosen_msg = np.random.choice(message_selection)
        channel.basic_publish(exchange='',
                              routing_key='hello',
                              body=chosen_msg)

        print(f" [x] Sent '{chosen_msg}'")

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

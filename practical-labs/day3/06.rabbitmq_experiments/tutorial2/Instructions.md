# RabbitMQ Experiment 2

Let's extend on our first experiment. Build a producer that:
1. waits between 0.1 - 2 seconds between sending messages
2. sends a total of 100 messages
3. randomly choses a greeting from a list of at least 3 alternatives

Edit the consumer so that it:
1. Waits between 0-1 seconds before printing out the message it received
2. Prints the message in uppercase

To do this you will need the following libraries and functions:

- time.sleep
- numpy - chose an appropriate random function. Check out np.random.choice for one part of the problem

# Turning our message queue into a job dispatching System

So far we have had one producer and one consumer operating on our queue but we might want to be able to distribute the work out to multiple consumers.

To do that we need to be able to distribute the work out. There are different appraoches we can take:

- Round-robin dispatching
- Fair dispatch

We will also talk about making message queues durable and resilient.

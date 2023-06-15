# Prefect Introduction
## A data pipelining framework

[Prefect](https://www.prefect.io/opensource/) is an open-source Pthon framework that allows us to chain Python tasks together into workflows.

This is a very quick introduction with two example workflow files:
- `prefect_test1.py`
- `prefect_test2.py`

The first script replicates the first example from the Prefect documentation.

The second script extends this with a new set of tasks and additional workflow that is run together within the same master script.

## Monitoring of the pipeline

During the workshop we didn't have time to go into the depths of monitoring these workflows but the concept was demonstrated using the free Prefect cloud account tier. It is left to the students to explore this themselves if this is of specific interest.

Tutorials and instructions are available [on the official website, here](https://docs.prefect.io/2.10.13/cloud/).
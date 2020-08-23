# Decoupled Celery example

This repo is an example of how the [Celery](https://docs.celeryproject.org/en/stable/) application and Celery worker can be decoupled and executed in different containers.

![demo](assets/demo.gif)

## System diagram

![system-diagram](assets/system-diagram-200822.png)

## Pre-requisite

- `docker-compose`
- `make`

## Getting started

```bash
# Use make to run docker-compose
make recompose
```

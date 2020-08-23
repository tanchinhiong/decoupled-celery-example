import time
import random

from celery import Celery

# Wait for rabbitmq to be started
time.sleep(15)

app = Celery(
    'postman',
    broker='amqp://user:bitnami@rabbitmq',
    backend='amqp://user:bitnami@rabbitmq',
)


@app.task(name='addTask')  # Named task
def add(x, y):
    print('Task Add started')
    time.sleep(10 * random.random())  # Simulate a long task
    print('Task Add done')
    return x + y

```plantuml
left to right direction
title Decoupled Celery example
actor "Developer" as dev

database "RabbitMQ" as rabbitmq
rectangle "Flower" as flower
rectangle "Celery application" as application
rectangle "Celery worker" as worker

dev --> flower
flower --> rabbitmq
rabbitmq <-- application
rabbitmq <-- worker
```

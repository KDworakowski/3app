#!/usr/bin/env python
import pika
import json
import config as cfg
import jsonschema
from jsonschema import validate

import requests


# Connect to RabbitMQ and create channel
connection = pika.BlockingConnection(pika.ConnectionParameters(host=cfg.RABBIT_HOST))
channel = connection.channel()

# Declare queue to send data
channel.queue_declare(queue=cfg.QUEUE_TOPIC)

data = {
        "id": "1",
        "name": "My Name",
        "description": 1
    }

# Convert python object to JSON
message = json.dumps(data)
response = requests.post('https://httpbin.org/post', json=message)




channel.basic_publish(exchange='', routing_key=cfg.QUEUE_TOPIC, body=message)
print(" [x] Sent data to RabbitMQ")
connection.close()

print("Status code: ", response.status_code)
print("Printing Entire Post Request")
print(response.json())

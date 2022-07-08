#!/usr/bin/env python
import pika
import json
import config as cfg
from jsonschema import validate



# Connect to RabbitMQ and create channel
connection = pika.BlockingConnection(pika.ConnectionParameters(host=cfg.RABBIT_HOST))
channel = connection.channel()

# Declare queue to send data
channel.queue_declare(queue=cfg.QUEUE_TOPIC)

# JSON
data = {
        "id": "1",
        "name": "My Name",
        "description": "This is description about me"
    }

# Schema for JSON Validating
schema = {
    "type" : "object",
    "properties" : {
        "id" : {"type" : "string"},
        "name" : {"type" : "string"},
        "description" : {"type" : "string"},
    },
}

#Validate json
validate(instance=data, schema=schema)
print(data)

# Convert python object to JSON
message = json.dumps(data)


# Send data
channel.basic_publish(exchange='', routing_key=cfg.QUEUE_TOPIC, body=message)
print(" [x] Sent data to RabbitMQ")
connection.close()

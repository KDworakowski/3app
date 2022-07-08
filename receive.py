#!/usr/bin/env python
import pika
import json
import config as cfg

import redis
from redis.commands.json.path import Path

# Connect to RabbitMQ and create channel
connection = pika.BlockingConnection(pika.ConnectionParameters(host=cfg.RABBIT_HOST))
channel = connection.channel()

# Declare and listen queue
channel.queue_declare(queue=cfg.QUEUE_TOPIC)

print(' [*] Waiting for messages. To exit press CTRL+C')

# Function process and print data
def callback(ch, method, properties, body):
    print("Method: {}".format(method))
    print("Properties: {}".format(properties))

    data = json.loads(body)
    print("ID: {}".format(data['id']))
    print("Name: {}".format(data['name']))
    print('Description: {}'.format(data['description']))

# Listen and receive data from queue
channel.basic_consume(cfg.QUEUE_TOPIC, callback, auto_ack=True)
channel.start_consuming()


client = redis.Redis(host='localhost', port=6379, db=0)

jane = {
     'name': "Jane",
     'Age': 33,
     'Location': "Chawton"
   }

client.json().set('id:1', Path.root_path(), "1")

result = client.json().get('person:1')
print(result)

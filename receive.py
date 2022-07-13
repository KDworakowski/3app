#!/usr/bin/env python
import pika
import json
import config as cfg
import pymongo

# Create a connection to MongoDB and create DB

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient.database_sample
my_collection = db["database"]

# Connect to RabbitMQ and create channel
connection = pika.BlockingConnection(pika.ConnectionParameters(host=cfg.RABBIT_HOST, port=cfg.PORT))
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
    my_collection.insert_one(data)
    print("Data sent to MongoDB:")

# Listen and receive data from queue
channel.basic_consume(cfg.QUEUE_TOPIC, callback, auto_ack=True)
channel.start_consuming()

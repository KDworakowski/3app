import pika
import time
import os
import pymongo
import json

# Create a connection to MongoDB and create DB

# myclient = pymongo.MongoClient("mongo:27017", username='root', password='password')
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient.database_sample
my_collection = db["database"]

# read rabbitmq connection url from environment variable
amqp_url = os.environ['AMQP_URL']
url_params = pika.URLParameters(amqp_url)

# connect to rabbitmq
connection = pika.BlockingConnection(url_params)
chan = connection.channel()

# declare a new queue
# durable flag is set so that messages are retained
# in the rabbitmq volume even between restarts
chan.queue_declare(queue='hello', durable=True)


def receive_msg(ch, method, properties, body):
    """function to receive the message from rabbitmq
    print it
    sleep for 2 seconds
    ack the message"""
    print('received msg : ', body.decode('utf-8'))
    time.sleep(2)
    print('acking it')
    ch.basic_ack(delivery_tag=method.delivery_tag)
    data = json.loads(body)
    my_collection.insert_one(data)
    print("DATA INSERTED TO MONGO: ", data)


# to make sure the consumer receives only one message at a time
# next message is received only after acking the previous one

chan.basic_qos(prefetch_count=1)

# define the queue consumption
chan.basic_consume(queue='hello',
                   on_message_callback=receive_msg)

print("Waiting to consume")
# start consuming
chan.start_consuming()

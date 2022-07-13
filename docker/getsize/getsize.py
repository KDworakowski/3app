#!/usr/bin/env python
import pymongo

# Create a connection to MongoDB and create DB

myclient = pymongo.MongoClient("mongo:27017", username='root', password='password')
db = myclient.database_sample
my_collection = db["database"]


# Count number of documents in database
numberOfDocs = my_collection.count_documents({})
print("The number of documents in collection : ", numberOfDocs)

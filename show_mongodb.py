#!/usr/bin/env python

import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.database_sample
customers = db["customers"]
for x in customers.find():
    print(x)

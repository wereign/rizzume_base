from dotenv import load_dotenv
from pymongo import MongoClient
import os
import json

load_dotenv()
connection_string = os.environ.get('CONNECTION_STRING')

client = MongoClient(connection_string)
db = client.rizzume
collection = db['rizzume_users']

def add_user(path):
    with open(path,'r') as jf:
        aarav_document = json.load(jf)


    collection.insert_one(aarav_document)


if __name__ == "__main__":
    add_user('./fake_data/aarav.json')



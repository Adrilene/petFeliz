from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config import urlMongo

# Replace the placeholder with your Atlas connection string
uri = urlMongo

# Set the Stable API version when creating a new client
client = MongoClient(uri, server_api=ServerApi('1'))
                          
mydb = client["testDatabase"]
mycol = mydb["testCollection"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

print(client.list_database_names())
print(mydb.list_collection_names())
print(x.inserted_id)
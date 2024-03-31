from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import os
import json

load_dotenv()

class PetsDatabase():
    def __init__(self):
        self.client = MongoClient(os.getenv('URI_MONGO'), server_api=ServerApi('1'))
        self.database = self.client["PetFeliz"]
        self.collection = self.database["Pets"]
        
    def inserir_pet(self, pet):
        # petJson = json.dumps(pet.__dict__)
        inserted = self.collection.insert_one(pet.__dict__)
        if inserted.inserted_id:
            return True
        return False

    def ver_pet(self, busca):
        return self.collection.find(busca)
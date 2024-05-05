from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

import os

load_dotenv()

class PetModel():

    def __init__(self):
        self.client = MongoClient(os.getenv('URI_MONGO'), server_api=ServerApi('1'))
        self.database = self.client["PetFeliz"]
        self.collection = self.database["Pets"]
        
    def inserir_pet(self, pet):
        inserted = self.collection.insert_one(pet)
        try:
            return inserted.inserted_id
        except:
            return False

    def ver_pet(self, busca):
        return self.collection.find(busca)

    def ver_todos_pets(self):
        petsDB = list(self.collection.find())
        return petsDB

    def alterar_pet(self, pet_id, alteracao):
        try:
            self.collection.find_one_and_update(
                {'_id': ObjectId(pet_id)},
                {'$set': alteracao}
            )
            return True
        except:
            return False
        
    def excluir_pet(self, pet_id):
        self.collection.find_one_and_delete(
            {'_id': ObjectId(pet_id)}
        )
    
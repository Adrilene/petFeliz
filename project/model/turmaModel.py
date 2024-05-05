import os

from bson.objectid import ObjectId
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()


class TurmaModel:
    def __init__(self):
        self.client = MongoClient(os.getenv("URI_MONGO"), server_api=ServerApi("1"))
        self.database = self.client["PetFeliz"]
        self.collection = self.database["Turmas"]

    def inserir_turma(self, turma):
        inserted = self.collection.insert_one(turma)
        try:
            return inserted.inserted_id
        except:
            return False

    def ver_todas_as_turmas(self):
        turmasDB = list(self.collection.find())
        return turmasDB

    def ver_uma_turma(self, turma_id):
        return self.collection.find_one({'_id': turma_id})


    def alterar_turma(self, turma_id, alteracao):
        try:
            self.collection.find_one_and_update(
                {'_id': ObjectId(turma_id)},
                {'$set': alteracao}
            )
            return True
        except:
            return False
    
    def adicionar_pet(self, turma_id, pet_id):
        self.collection.find_one_and_update(
            {'_id': ObjectId(turma_id)},
            {'$push': {'pets': pet_id}}
        )

    def excluir_turma(self, turma_id):
        self.collection.find_one_and_delete(
            {'_id': ObjectId(turma_id)}
        )

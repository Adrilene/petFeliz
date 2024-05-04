from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import os


load_dotenv()


class TurmaModel:
    def __init__(self):
        self.client = MongoClient(os.getenv("URI_MONGO"), server_api=ServerApi("1"))
        self.database = self.client["PetFeliz"]
        self.collection = self.database["Turmas"]

    def inserir_turma(self, turma):
        inserted = self.collection.insert_one(turma.__dict__)
        if inserted.inserted_id:
            return True
        return False

    def ver_todas_as_turmas(self):
        turmasDB =  list(self.collection.find())
        return turmasDB


    def adicionar_pet(self, turma_id, pet_id):
        self.collection.find_one_and_update(
            {'_id': turma_id},
            {'$push': {'pets': pet_id}}
        )


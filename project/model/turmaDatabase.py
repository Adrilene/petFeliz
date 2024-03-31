class turmaDatabase():
    def __init__(self):
        self.client = MongoClient(uriMongo, server_api=ServerApi('1'))
        self.database = self.client["PetFeliz"]
        self.collection = self.database["Turmas"]

    
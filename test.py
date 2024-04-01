# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
# from config import urlMongo

# # Replace the placeholder with your Atlas connection string
# uri = urlMongo

# # Set the Stable API version when creating a new client
# client = MongoClient(uri, server_api=ServerApi('1'))
                          
# mydb = client["testDatabase"]
# mycol = mydb["testCollection"]

# mydict = { "name": "John", "address": "Highway 37" }

# x = mycol.insert_one(mydict)

# print(client.list_database_names())
# print(mydb.list_collection_names())
# print(x.inserted_id)

import requests
def get_endereco(endereco):
        
    url = f"https://viacep.com.br/ws/{endereco['cep']}/json/"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    enderecoCompleto = {
        "Rua": response.json()['logradouro'],
        "Bairro": response.json()['bairro'],
        "Cidade": response.json()['localidade'],
        "Estado": response.json()['uf'],
        "Numero": endereco['numero']
    }

    return enderecoCompleto

print(get_endereco({'cep': '60870520', 'numero': '1598'}))
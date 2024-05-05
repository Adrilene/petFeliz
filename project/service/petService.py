import requests
from project.model.petModel import PetModel
from project.model.turmaModel import TurmaModel


def check_pet(pet):
    mandatory_fields = ["nome", "tutor", "endereco", "tipo"]
    for field in mandatory_fields:
        if field not in pet.keys():
            return False, f"{field} não encontrado"

    if pet["tipo"] == "cachorro" and "porte" not in pet.keys():
        return False, f"Obrigatório definir porte para cachorro"

    return True, "Ok"


def definir_turma(pet):
    turmas = TurmaModel().ver_todas_as_turmas()

    for turma in turmas:
        if turma['tipo_pet'] == pet['tipo'] and turma['porte_pet'] == pet['porte']:
            return turma
    
    return False


def definir_turma_todos():
    pets = PetModel().ver_todos_pets()

    for pet in pets:
        turma = definir_turma(pet)
        if turma:
            if pet['_id'] not in turma['pets']:
                TurmaModel().adicionar_pet(turma['_id'], pet['_id'])
                PetModel().alterar_pet(pet['_id'], {'turma': turma['_id']})


def get_endereco_completo(endereco):

    url = f"https://viacep.com.br/ws/{endereco['cep']}/json/"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    enderecoCompleto = {
        "Rua": response.json()["logradouro"],
        "Bairro": response.json()["bairro"],
        "Cidade": response.json()["localidade"],
        "Estado": response.json()["uf"],
        "Numero": endereco["numero"],
    }

    return enderecoCompleto

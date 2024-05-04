import requests

from project.model.turma import TurmaDatabase

class Pet():
    def __init__(self, nome, tutor, endereco, contato, tipo, porte=None):
        self.nome = nome
        self.tutor = tutor
        self.endereco = self.get_endereco_completo(endereco)
        self.contato = contato
        self.tipo = tipo
        self.porte = porte
        self.turma = ''

    def definir_turma(self):
        turmas = TurmaDatabase().ver_todas_as_turmas()

        for turma in turmas:
            if turma.tipo_pet == self.tipo and turma.porte_pet == self.porte:
                self.turma = turma['nome']
                TurmaDatabase().adicionar_pet(self, )


    def get_endereco_completo(self, endereco):
        
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
        

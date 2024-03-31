import requests

class Pet():
    def __init__(self, nome, tutor, endereco, contato, tipo, porte=None):
        self.nome = nome
        self.tutor = tutor
        self.endereco = self.get_endereco(endereco)
        self.contato = contato
        self.tipo = tipo
        self.porte = porte
        self.turma = ''

    def definir_turma(self, porte):
        pass

    def get_endereco(self, endereco):
        
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
        

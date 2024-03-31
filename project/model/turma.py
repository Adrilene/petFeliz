class Turma():
    def __init__(self, nome, tipo, porte=None):
        self.nome = nome
        self.tipo = tipo
        self.porte = porte
        self.pets = []

    def adicionar_pet(self, pet):
        self.pets.append(pet)
from project import app
from flask import request, jsonify

from project.model.pet import Pet
from project.model.petsDatabase import PetsDatabase

@app.route('/', methods=['GET'])
def hello():
    return "Hello, it's working!"

@app.route('/verPets', methods=['GET'])
def verPets():
    return ''

@app.route('/cadastrarPet', methods=["POST"])
def cadastrarPet():
    newPet = Pet(
        nome = request.json['nome'],
        tutor = request.json['tutor'],
        endereco= request.json['endereco'],
        contato= request.json['contato'],
        tipo = request.json['tipo'],
        porte = request.json['porte'] if 'porte' in request.json.keys() else None
    )

    if PetsDatabase().inserir_pet(newPet):
        return jsonify(f'Pet {newPet.nome} cadastrado com sucesso'), 201
    
    return jsonify(f'Erro ao cadastrar o Pet {newPet.nome}'), 400

@app.route('/cadastrarTurma', methods=['POST'])
def cadastrarTurma():
    return ''
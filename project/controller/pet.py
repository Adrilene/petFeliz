from project import app
from flask import request, jsonify

from project.model.pet import Pet
from project.model.pet import PetDatabase
from project.model.turma import Turma
from project.model.turma import TurmaDatabase

@app.route('/verTodosPets', methods=['GET'])
def ver_todos_pets():
    return ''

@app.route('/cadastrarPet', methods=["POST"])
def cadastrar_pet():
    new_pet = Pet(
        nome = request.json['nome'],
        tutor = request.json['tutor'],
        endereco= request.json['endereco'],
        contato= request.json['contato'],
        tipo = request.json['tipo'],
        porte = request.json['porte'] if 'porte' in request.json.keys() else None
    )
    new_pet.definir_turma()
    
    if PetDatabase().inserir_pet(new_pet):
        return jsonify(f'Pet {new_pet.nome} cadastrado com sucesso'), 201
    
    return jsonify(f'Erro ao cadastrar o Pet {new_pet.nome}'), 400


@app.route('/definirTurmas', methods=['GET'])
def definir_turmas():
    if Pet.definir_turma_todos():
        return jsonify(f'Todas as turmas definidas!'), 200
    return jsonify('Erro ao definir as turmas'), 500

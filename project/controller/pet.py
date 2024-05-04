from unittest import result
from project import app
from flask import request, jsonify

from project.model.petModel import PetModel
from project.model.turmaModel import TurmaModel
from project.service.petService import check_pet, get_endereco_completo, definir_turma


@app.route('/verTodosPets', methods=['GET'])
def ver_todos_pets():
    return ''

@app.route('/cadastrarPet', methods=["POST"])
def cadastrar_pet():
    
    result, msg = check_pet(request.json)

    if result:
        try:
            endereco = get_endereco_completo(request.json['endereco'])
        except:
            return jsonify('CEP não encontrado'), 400
        
        new_pet = {
            "nome": request.json['nome'].lower(),
            "tutor": request.json['tutor'].lower(),
            "endereco":endereco,
            "contato": request.json['contato'],
            "tipo": request.json['tipo'].lower(),
            "porte": request.json['porte'].lower() if 'porte' in request.json.keys() else None
        }

        try:
            turma = definir_turma(new_pet)
            if turma:
                new_pet['turma'] = turma['_id']
                
            
            if PetModel().inserir_pet(new_pet):
                if not turma:
                    return jsonify(f'Pet {new_pet.nome} cadastrado, mas está sem turma'), 201
                return jsonify(f"Pet {new_pet.nome} cadastrado na turma {turma['nome']}"), 201

        except:
            return jsonify('Erro de acesso ao banco de dados'), 500

    
    else:
        return jsonify(msg), 400


@app.route('/definirTurmas', methods=['GET'])
def definir_turmas():
    if PetModel.definir_turma_todos():
        return jsonify(f'Todas as turmas definidas!'), 200
    return jsonify('Erro ao definir as turmas'), 500

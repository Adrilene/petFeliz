from project import app
from flask import request, jsonify

from project.model.turma import Turma
from project.model.turmaDatabase import TurmaDatabase

@app.route('/cadastrarTurma', methods=['POST'])
def cadastrar_turma():
    new_turma = Turma(
        nome = request.json['nome'],
        tipo_pet = request.json['tipo_pet'],
        porte_pet = request.json['porte_pet'] if 'porte_pet' in request.json.keys() else None
    )

    if TurmaDatabase().inserir_turma(new_turma):
        return jsonify(f'Turma {new_turma.nome} cadastrada com sucesso'), 201
    
    return jsonify(f'Erro ao cadastrar a Turma {new_turma.nome}'), 400

@app.route('/verTodasTurmas', methods=['GET'])
def ver_todas_turmas():
    return ''
import json
from urllib import response
from project import app
from flask import request, jsonify

from project.model.turmaModel import TurmaModel
from project.service.turmaService import check_turma


@app.route('/cadastrarTurma', methods=['POST'])
def cadastrar_turma():
    result, msg = check_turma(response.json)
    if result:
        new_turma = {
            "nome": request.json['nome'].lower(),
            "tipo_pet": request.json['tipo_pet'].lower(),
            "porte_pet": request.json['porte_pet'] if 'porte_pet' in request.json.keys() else None
        }

        try:
            if TurmaDatabase().inserir_turma(new_turma):
                return jsonify(f'Turma {new_turma.nome} cadastrada com sucesso'), 201
        except:
            return jsonify('Erro de acesso ao banco de dados'), 500
    
    else:
        return jsonify(msg), 400

@app.route('/verTodasTurmas', methods=['GET'])
def ver_todas_turmas():
    turmas = TurmaModel().ver_todas_as_turmas()
    resposta = []
    for turma in turmas:
        resposta.append({"nome": turma.nome, "pets": turma.pets})

    return jsonify(resposta), 200
    
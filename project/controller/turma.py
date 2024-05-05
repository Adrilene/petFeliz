import json
from urllib import response
from project import app
from flask import request, jsonify
from unidecode import unidecode

from project.model.turmaModel import TurmaModel
from project.service.turmaService import check_turma


@app.route('/cadastrarTurma', methods=['POST'])
def cadastrar_turma():
    result, msg = check_turma(request.json)
    if result:
        new_turma = {
            "nome": request.json['nome'],
            "tipo_pet": request.json['tipo_pet'].lower(),
            "porte_pet": unidecode(request.json['porte_pet'].lower()) if 'porte_pet' in request.json.keys() else None,
            "pets": []
        }


        if TurmaModel().inserir_turma(new_turma):
            return jsonify(f"Turma {new_turma['nome']} cadastrada com sucesso"), 201
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
    

@app.route("/alterarTurma", methods=["GET"])
def alterar_turma():
    alteracao = request.args.to_dict()
    turma_id = alteracao["turma_id"]

    if TurmaModel().alterar_turma(turma_id, alteracao):
        return jsonify("Turma alterado com sucesso"), 200

    else:
        return jsonify("Erro de conexão com o banco"), 500


@app.route("/excluirTurma/<turma_id>", methods=["GET"])
def excluir_turma(turma_id):
    TurmaModel().excluir_turma(turma_id)

    return jsonify("Turma excluído com sucesso"), 200
from project import app
from flask import request, jsonify

from project.model.petModel import PetModel
from project.model.turmaModel import TurmaModel
from project.service.petService import (
    check_pet,
    get_endereco_completo,
    definir_turma,
    definir_turma_todos,
    get_todos_pets
)


@app.route("/verTodosPets", methods=["GET"])
def ver_todos_pets():
    return get_todos_pets()


@app.route("/cadastrarPet", methods=["POST"])
def cadastrar_pet():

    result, msg = check_pet(request.json)

    if result:
        try:
            endereco = get_endereco_completo(request.json["endereco"])
        except:
            return jsonify("CEP não encontrado"), 400

        new_pet = {
            "nome": request.json["nome"],
            "tutor": request.json["tutor"],
            "endereco": endereco,
            "contato": request.json["contato"],
            "tipo": request.json["tipo"].lower(),
            "porte": (
                request.json["porte"].lower()
                if "porte" in request.json.keys()
                else None
            ),
        }

        try:
            turma = definir_turma(new_pet)
            if turma:
                new_pet["turma"] = turma["_id"]

            pet_id = PetModel().inserir_pet(new_pet)
            if pet_id:
                if not turma:
                    return (
                        jsonify(f"Pet {new_pet.nome} cadastrado, mas está sem turma"),
                        201,
                    )
                TurmaModel().adicionar_pet(new_pet["turma"], pet_id)
                return (
                    jsonify(f"Pet {new_pet.nome} cadastrado na turma {turma['nome']}"),
                    201,
                )

        except:
            return jsonify("Erro de acesso ao banco de dados"), 500

    else:
        return jsonify(msg), 400


@app.route("/definirTurmas", methods=["GET"])
def definir_turmas():
    definir_turma_todos()
    return jsonify(f"Todas as turmas definidas!"), 200


@app.route("/alterarPet", methods=["PATCH"])
def alterar_pet():
    alteracao = request.args.to_dict()
    pet_id = alteracao["pet_id"]

    if PetModel().alterar_pet(pet_id, alteracao):
        return jsonify("Pet alterado com sucesso"), 200

    else:
        return jsonify("Erro de conexão com o banco"), 500


@app.route("/excluirPet/<pet_id>", methods=["DELETE"])
def excluir_pet(pet_id):
    PetModel().excluir_pet(pet_id)

    return jsonify("Pet excluído com sucesso"), 200

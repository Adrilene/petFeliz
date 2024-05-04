def check_turma(turma):
    mandatory_fields = ["nome", "tipo_pet""]
    for field in mandatory_fields:
        if field not in turma.keys():
            return False, f"{field} não encontrado"

    if turma["tipo_pet"] == "cachorro" and "porte" not in turma.keys():
        return False, f"Obrigatório definir porte para cachorro"

    return True, "Ok"
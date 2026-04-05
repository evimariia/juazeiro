from application.app.models.alunos import buscar_aluno_por_rfid
from application.app.models.aula import buscar_aula, criar_aula
from application.app.models.matricula import buscar_aluno_por_ra, validar_matricula
from application.app.models.presenca import inserir_presenca
from application.app.models.sala import buscar_sala_por_dispositivo
from application.app.models.turma import buscar_turma

def registrar_primeira_presenca_service(id_dispositivo, rfid_uid):

    id_sala = buscar_sala_por_dispositivo(id_dispositivo)
    ra_aluno = buscar_aluno_por_rfid(rfid_uid)

    id_turma = buscar_turma(id_sala, ra_aluno)

    if buscar_aula(id_turma):
        id_aula = buscar_aula(id_turma)
    else:
        id_aula = criar_aula(id_turma)

    if validar_matricula(ra_aluno, id_turma):
        id_matricula_aluno = buscar_aluno_por_ra(ra_aluno)
        inserir_presenca(id_aula, id_matricula_aluno)
        return True, id_aula
    else:
        print(f"Aluno com RA {ra_aluno} não está matriculado na turma {id_turma}.")
        return False

def registrar_presenca_service(rfid_uid, id_aula):
    ra_aluno = buscar_aluno_por_rfid(rfid_uid)
    id_matricula_aluno = buscar_aluno_por_ra(ra_aluno)
    inserir_presenca(id_aula, id_matricula_aluno)
    return True
from application.app.models.alunos import buscar_aluno_por_rfid
from application.app.models.aula import buscar_aula, criar_aula
from application.app.models.matricula import buscar_aluno_por_ra, validar_matricula
from application.app.models.presenca import inserir_presenca
from application.app.models.sala import buscar_sala_por_dispositivo
from application.app.models.turma import buscar_turma

def registrar_presenca_completo_service(id_dispositivo, rfid_uid):
    id_sala = buscar_sala_por_dispositivo(id_dispositivo)
    ra_aluno = buscar_aluno_por_rfid(rfid_uid)
    
    if not ra_aluno:
        return False, "Cartão RFID não cadastrado"

    id_turma = buscar_turma(id_sala, ra_aluno)
    
    if not id_turma:
        return False, "Turma não encontrada para esta sala/aluno"

    # Se a aula não existir, cria. Se existir, recupera.
    id_aula = buscar_aula(id_turma)
    if not id_aula:
        id_aula = criar_aula(id_turma)

    if validar_matricula(ra_aluno, id_turma):
        id_matricula_aluno = buscar_aluno_por_ra(ra_aluno)
        
        # Opcional: verificar se o aluno já bateu o cartão NESTA aula para não duplicar
        # if not buscar_presenca_por_aula_e_aluno(id_aula, id_matricula_aluno):
        
        inserir_presenca(id_aula, id_matricula_aluno)
        return True, "Presença registrada com sucesso"
    
    return False, "Aluno não matriculado nesta turma"
# from application.app.models.alunos import buscar_aluno_por_rfid
# from application.app.models.aula import buscar_aula_hoje, criar_aula
# from application.app.models.matricula import buscar_aluno_por_ra, validar_matricula
# from application.app.models.presenca import inserir_presenca
# from application.app.models.sala import buscar_sala_por_dispositivo
# from application.app.models.turma import buscar_turma
from application.app.models.professor import buscar_professor_por_ra, validar_senha_prof

def login_professor_service(ra_professor, senha):
    if buscar_professor_por_ra(ra_professor):
        if validar_senha_prof(senha):
            return True
    else:
        return False
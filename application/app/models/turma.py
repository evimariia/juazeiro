from application.database.connection import get_connection
from application.app.utils import dia_da_semana_atual, semestre_atual, turno_atual

def buscar_turma(id_sala, ra_aluno):
    db_conn = get_connection()
    cursor = db_conn.cursor()

    dia_da_semana = dia_da_semana_atual()
    turno = turno_atual()
    semestre_oferta = semestre_atual()

    busca_turma = """
    SELECT T.id_turma FROM tb_turmas T
    JOIN tb_matricula_turma M ON T.id_turma = M.id_turma
    WHERE T.id_sala = %s AND M.ra_aluno = %s
    AND T.dia_semana = %s
    AND T.turno = %s
    AND T.semestre_oferta = %s
    """
    
    cursor.execute(busca_turma, (id_sala, ra_aluno, dia_da_semana, turno, semestre_oferta))
    turma = cursor.fetchone()

    cursor.close()
    db_conn.close()

    return turma[0]
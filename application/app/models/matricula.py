from database.connection import get_connection

def buscar_aluno_por_ra(ra_aluno):
    db_conn = get_connection()
    cursor = db_conn.cursor()

    busca_aluno = "SELECT id_matricula_turma FROM tb_matriculas WHERE ra_aluno = %s"
    cursor.execute(busca_aluno, (ra_aluno,))
    aluno = cursor.fetchall()

    cursor.close()
    db_conn.close()

    return aluno[0]

def validar_matricula(ra_aluno, id_turma):
    db_conn = get_connection()
    cursor = db_conn.cursor()

    busca_matricula = "SELECT id_matricula_turma FROM tb_matriculas WHERE ra_aluno = %s AND id_turma = %s"
    cursor.execute(busca_matricula, (ra_aluno, id_turma))
    matricula = cursor.fetchone()

    cursor.close()
    db_conn.close()

    if matricula:
        return True
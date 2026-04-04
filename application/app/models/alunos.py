from database.connection import get_connection

def buscar_aluno_por_rfid(rfid_uid):
    db_conn = get_connection()
    cursor = db_conn.cursor()

    busca_aluno = "SELECT ra_aluno FROM tb_alunos WHERE rfid_uid = %s"
    cursor.execute(busca_aluno, (rfid_uid,))
    aluno = cursor.fetchone()

    cursor.close()
    db_conn.close()

    return aluno
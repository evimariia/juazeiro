from application.database.connection import get_connection

def buscar_professor_por_ra(ra_professor):
    db_conn = get_connection()
    cursor = db_conn.cursor()

    busca_professor = "SELECT ra_professor FROM tb_professores WHERE ra_professor = %s"
    cursor.execute(busca_professor, (ra_professor,))
    professor = cursor.fetchone()

    cursor.close()
    db_conn.close()

    return professor[0]

def validar_senha_prof(senha):
    return True
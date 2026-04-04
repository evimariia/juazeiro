from database.connection import get_connection
from app.utils import hoje

def buscar_turma(id_turma):
    db_conn = get_connection()
    cursor = db_conn.cursor()

    data = hoje()

    busca_aula = """
    SELECT id_aula FROM tb_aulas
    WHERE id_turma = %s AND data_aula = %s
    """
    
    cursor.execute(busca_aula, (id_turma, data))
    aula = cursor.fetchone()

    cursor.close()
    db_conn.close()

    return aula

def criar_aula(id_turma):
    db_conn = get_connection()
    cursor = db_conn.cursor()

    data = hoje()

    insert_aula = """
    INSERT INTO tb_aulas (id_turma, data_aula, permissao_validar)
    VALUES (%s, %s, FALSE)
    """
    try:
        cursor.execute(insert_aula, (id_turma, data))
        db_conn.commit()
        return True
    except Exception as e:
        print(f"Não foi possível criar a aula: {e}")
        db_conn.rollback()
        return False
    finally:
        cursor.close()
        db_conn.close()     
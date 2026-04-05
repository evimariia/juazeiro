from application.database.connection import get_connection
from application.app.utils import hoje

def buscar_aula(id_turma):
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

    return aula[0]

def criar_aula(id_turma):
    db_conn = get_connection()
    cursor = db_conn.cursor()

    data = hoje()

    # 0 = bloqueado | 1 = validação liberada pelo professor
    insert_aula = """
    INSERT INTO tb_aulas (id_turma, data_aula, permissao_validar)
    VALUES (%s, %s, 0)
    """
    try:
        cursor.execute(insert_aula, (id_turma, data))
        db_conn.commit()
        return buscar_aula(id_turma)
    except Exception as e:
        print(f"Não foi possível criar a aula: {e}")
        db_conn.rollback()
        return False
    finally:
        cursor.close()
        db_conn.close()     
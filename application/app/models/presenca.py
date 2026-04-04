from database.connection import get_connection

def registrar_presenca(id_aula, id_matricula_aluno, situacao_presenca="VALIDACAO_PENDENTE"):
    db_conn = get_connection()
    cursor = db_conn.cursor()


    insert_presenca = """
    INSERT INTO tb_presenca (id_aula, id_matricula_aluno, situacao_presenca)
    VALUES (%s, %s, %s)
    """
    try:
        cursor.execute(insert_presenca, (id_aula, id_matricula_aluno, situacao_presenca))
        db_conn.commit()
        return True
    except Exception as e:
        print(f"Não foi possível registrar a presença: {e}")
        db_conn.rollback()
        return False
    finally:
        cursor.close()
        db_conn.close()        
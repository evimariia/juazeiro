from application.database.connection import get_connection

def buscar_disciplina(nome_disciplina):
    db_conn = get_connection()
    cursor = db_conn.cursor()

    busca_disciplina = """
    SELECT id_disciplina FROM tb_disciplinas
    WHERE nome_disciplina = %s
    """

    cursor.execute(busca_disciplina, (nome_disciplina,))
    disciplina = cursor.fetchone()

    cursor.close()
    db_conn.close()

    return disciplina[0]

'''
Notas não mentais:
- Criar uma função para buscar disciplina pelo nome que não precise exatamente do nome para ela retornar o nome certo da disciplina

'''
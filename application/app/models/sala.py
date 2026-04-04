from database.connection import get_connection

def buscar_sala_por_dispositivo(id_dispositivo):
    db_conn = get_connection()
    cursor = db_conn.cursor()

    busca_sala = "SELECT id_sala FROM tb_salas WHERE id_dispositivo = %s"
    cursor.execute(busca_sala, (id_dispositivo,))
    sala = cursor.fetchone()

    cursor.close()
    db_conn.close()

    return sala
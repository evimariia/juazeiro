from datetime import datetime
import flask
from database.connection import get_connection

@app.route('/presenca', methods=['POST'])
def registrar_presenca():
    dados = flask.request.get_json()  # recebe o JSON enviado pelo ESP32

    rfid_uid = dados.get('rfid_uid')
    id_aula = dados.get('id_aula')

    db_conn = get_connection()
    cursor = db_conn.cursor()

    hoje = datetime.now().date()
    busca_aluno = "SELECT ra_aluno FROM tb_alunos WHERE rfid_uid = %s"

    # Busca o aluno pelo UID da tag RFID
    cursor.execute(busca_aluno, (rfid_uid,))
    aluno = cursor.fetchone()

    if not aluno:
        return flask.jsonify({"status": "erro", "mensagem": "Aluno não encontrado"}), 404

    ra_aluno = aluno[0]

    registrar_presenca = """INSERT INTO tb_presenca (id_aula, ra_matricula_aluno, situacao_presenca)
           VALUES (%s, %s, 'REGISTRADA')"""

    # Registra a presença
    cursor.execute(registrar_presenca, (id_aula, ra_aluno))
    db_conn.commit()
    cursor.close()
    db_conn.close()

    return flask.jsonify({"status": "ok", "mensagem": "Presença registrada"}), 201
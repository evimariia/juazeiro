from datetime import datetime
from application.app import app
from application.app.models.alunos import buscar_aluno_por_rfid
from application.app.models.presenca import inserir_presenca
from application.app.services.presenca_service import registrar_presenca_service, registrar_primeira_presenca_service
import flask
from application.database.connection import get_connection

@app.route('/presenca', methods=['POST'])
def registrar_presenca():
    dados = flask.request.get_json()
    rfid_uid = dados.get('rfid_uid')
    id_dispositivo = dados.get('id_dispositivo')

    # 1. Validação de dados de entrada
    if not rfid_uid:
        return flask.jsonify({"status": "erro", "mensagem": "Não foi possível obter o UID do RFID"}), 400

    if not id_dispositivo:
        return flask.jsonify({"status": "erro", "mensagem": "Não foi possível obter o ID do dispositivo"}), 400

    try:
        # 2. Chama um serviço que decide o que fazer
        # Esse serviço deve verificar no banco: "Já existe aula aberta?"
        # Se não existir, ele cria (primeira presença). Se existir, ele apenas vincula.
        sucesso = registrar_presenca_service(rfid_uid, id_dispositivo)

        if sucesso:
            return flask.jsonify({"status": "ok", "mensagem": "Presença registrada"}), 201
        else:
            return flask.jsonify({"status": "erro", "mensagem": "Falha no registro"}), 500

    except Exception as e:
        # Captura erros de banco ou lógica para o Flask não travar
        return flask.jsonify({"status": "erro", "mensagem": str(e)}), 500
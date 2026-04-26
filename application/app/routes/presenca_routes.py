from application.app.services.presenca_service import registrar_presenca_service
from flask import Blueprint, Flask

auth_presenca_rota = Blueprint('auth_presenca_rota', __name__)

@auth_presenca_rota.route('/presenca', methods=['POST'])
def registrar_presenca():
    dados = Flask.request.get_json()
    rfid_uid = dados.get('rfid_uid')
    id_dispositivo = dados.get('id_dispositivo')

    # 1. Validação de dados de entrada
    if not rfid_uid:
        return Flask.jsonify({"status": "erro", "mensagem": "Não foi possível obter o UID do RFID"}), 400

    if not id_dispositivo:
        return Flask.jsonify({"status": "erro", "mensagem": "Não foi possível obter o ID do dispositivo"}), 400

    try:
        # 2. Chama um serviço que decide o que fazer
        # Esse serviço deve verificar no banco: "Já existe aula aberta?"
        # Se não existir, ele cria (primeira presença). Se existir, ele apenas vincula.
        resultado, mensagem = registrar_presenca_service(id_dispositivo, rfid_uid)

        if resultado:
            return Flask.jsonify({"status": "ok", "mensagem": "Presença registrada"}), 201
        else:
            return Flask.jsonify({"status": "erro", "mensagem": mensagem}), 500

    except Exception as e:
        # Captura erros de banco ou lógica para o Flask não travar
        return Flask.jsonify({"status": "erro", "mensagem": str(e)}), 500
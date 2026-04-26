import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from unittest.mock import patch
from application.app.app import app

# ============================================================
#  Configuração
# ============================================================

app.config['TESTING'] = True


# ============================================================
#  Testes de validação de entrada (sem banco)
# ============================================================

# def test_registrar_presenca_sem_rfid_uid():
#     """Deve retornar 400 quando rfid_uid não for enviado"""
#     client = app.test_client()

#     response = client.post('/presenca', json={
#         "id_dispositivo": 1001
#     })

#     assert response.status_code == 400
#     assert response.get_json()["status"] == "erro"


# def test_registrar_presenca_sem_id_dispositivo():
#     """Deve retornar 400 quando id_dispositivo não for enviado"""
#     client = app.test_client()

#     response = client.post('/presenca', json={
#         "rfid_uid": "A1B2C3D4"
#     })

#     assert response.status_code == 400
#     assert response.get_json()["status"] == "erro"


# def test_registrar_presenca_sem_corpo():
#     """Deve retornar 400 quando nenhum dado for enviado"""
#     client = app.test_client()

#     response = client.post('/presenca', json={})

#     assert response.status_code == 400
#     assert response.get_json()["status"] == "erro"


# # ============================================================
# #  Testes de lógica da rota (com mock do service)
# # ============================================================

# @patch('application.app.routes.presenca_routes.registrar_presenca_service')
# def test_registrar_presenca_sucesso(mock_service):
#     """Deve retornar 201 quando o service retornar sucesso"""
#     mock_service.return_value = (True, "Presença registrada com sucesso")
#     client = app.test_client()

#     response = client.post('/presenca', json={
#         "rfid_uid": "A1B2C3D4",
#         "id_dispositivo": 1001
#     })

#     assert response.status_code == 201
#     assert response.get_json()["status"] == "ok"


''''
TESTAR NOVAMENTE
O código da rota trata qualquer retorno False do service como erro interno e devolve 500
'''
@patch('application.app.routes.presenca_routes.registrar_presenca_service')
def test_registrar_presenca_rfid_nao_cadastrado(mock_service):
    """Deve retornar 400 quando o RFID não estiver cadastrado"""
    mock_service.return_value = (False, "Cartão RFID não cadastrado")
    client = app.test_client()

    response = client.post('/presenca', json={
        "rfid_uid": "FFFFFFFF",
        "id_dispositivo": 1001
    })

    assert response.status_code == 400
    assert response.get_json()["status"] == "erro"
    assert response.get_json()["mensagem"] == "Cartão RFID não cadastrado"


# @patch('application.app.routes.presenca_routes.registrar_presenca_service')
# def test_registrar_presenca_turma_nao_encontrada(mock_service):
#     """Deve retornar 400 quando não houver turma para a sala/aluno"""
#     mock_service.return_value = (False, "Turma não encontrada para esta sala/aluno")
#     client = app.test_client()

#     response = client.post('/presenca', json={
#         "rfid_uid": "A1B2C3D4",
#         "id_dispositivo": 1001
#     })

#     assert response.status_code == 400
#     assert response.get_json()["status"] == "erro"


# @patch('application.app.routes.presenca_routes.registrar_presenca_service')
# def test_registrar_presenca_falha_no_service(mock_service):
#     """Deve retornar 500 quando o service lançar uma exceção inesperada"""
#     mock_service.side_effect = Exception("Erro inesperado no banco")
#     client = app.test_client()

#     response = client.post('/presenca', json={
#         "rfid_uid": "A1B2C3D4",
#         "id_dispositivo": 1001
#     })

#     assert response.status_code == 500
#     assert response.get_json()["status"] == "erro"
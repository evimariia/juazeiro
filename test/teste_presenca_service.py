import pytest
from unittest.mock import patch
from application.app.services.presenca_service import registrar_presenca_completo_service

@patch('application.app.services.presenca_service.buscar_sala_por_dispositivo')
@patch('application.app.services.presenca_service.buscar_aluno_por_rfid')
@patch('application.app.services.presenca_service.buscar_turma')
@patch('application.app.services.presenca_service.buscar_aula')
@patch('application.app.services.presenca_service.validar_matricula')
@patch('application.app.services.presenca_service.buscar_aluno_por_ra')
@patch('application.app.services.presenca_service.inserir_presenca')
def test_registrar_presenca_sucesso(
    mock_inserir, mock_buscar_ra, mock_validar, mock_buscar_aula, 
    mock_buscar_turma, mock_buscar_rfid, mock_buscar_sala
):
    # Configurando os retornos simulados (Mocks)
    mock_buscar_sala.return_value = 1
    mock_buscar_rfid.return_value = "A1B2C3D4"
    mock_buscar_turma.return_value = 10
    mock_buscar_aula.return_value = 3 # Aula já existe
    mock_validar.return_value = True
    mock_buscar_ra.return_value = 15 # ID da matrícula

    # Executa o serviço
    resultado = registrar_presenca_completo_service("1002","A1B2C3D4")[0]

    # Verificações
    assert resultado is True
    mock_inserir.assert_called_once_with(3, 15)
-- ============================================================
--  SISTEMA DE CONTROLE DE PRESENÇA VIA RFID
--  Trabalho de Conclusão de Curso — Engenharia de Computação
--  MySQL 8.0 | Windows
-- ============================================================

-- ============================================================
--  GERENCIAMENTO DE USUÁRIOS (Segurança)
-- ============================================================

-- Usuário de aplicação: acesso de leitura e escrita sem DDL
CREATE USER IF NOT EXISTS 'python_backend_service'@'localhost'
    IDENTIFIED WITH caching_sha2_password BY 'senha' --Substitua 'senha' por uma senha forte e segura
    FAILED_LOGIN_ATTEMPTS 5 PASSWORD_LOCK_TIME 1;

GRANT SELECT, INSERT, UPDATE ON db_juazeiro.* TO 'python_backend_service'@'localhost';

FLUSH PRIVILEGES;

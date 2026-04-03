-- ============================================================
--  SISTEMA DE CONTROLE DE PRESENÇA VIA RFID
--  Trabalho de Conclusão de Curso — Engenharia de Computação
--  MySQL 8.0 | Windows
-- ============================================================

-- ============================================================
--  GERENCIAMENTO DE USUÁRIOS (Segurança)
-- ============================================================

-- Usuário de aplicação: acesso de leitura e escrita sem DDL
CREATE USER IF NOT EXISTS 'app_rfid'@'localhost'
    IDENTIFIED WITH caching_sha2_password BY 'TrocaPelaS3nh@Forte!'
    PASSWORD EXPIRE INTERVAL 180 DAY
    FAILED_LOGIN_ATTEMPTS 5 PASSWORD_LOCK_TIME 1;

GRANT SELECT, INSERT, UPDATE ON db_presenca_rfid.* TO 'app_rfid'@'localhost';

-- Usuário de leitura: relatórios e consultas sem escrita
CREATE USER IF NOT EXISTS 'readonly_rfid'@'localhost'
    IDENTIFIED WITH caching_sha2_password BY 'OutraSenha@Forte2!'
    PASSWORD EXPIRE INTERVAL 180 DAY
    FAILED_LOGIN_ATTEMPTS 5 PASSWORD_LOCK_TIME 1;

GRANT SELECT ON db_presenca_rfid.* TO 'readonly_rfid'@'localhost';

FLUSH PRIVILEGES;
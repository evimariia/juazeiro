-- ============================================================
--  DADOS DE TESTE
--  Sistema de Controle de Presença via RFID
--  Executar APÓS a criação das tabelas
-- ============================================================

-- ------------------------------------------------------------
--  tb_alunos
-- ------------------------------------------------------------
INSERT INTO tb_alunos (ra_aluno, nome_aluno, situacao_aluno, rfid_uid) VALUES
(12345678, 'Ana Clara Souza',       'MATRICULADO', 'A1B2C3D4'),
(23456789, 'Bruno Henrique Lima',   'MATRICULADO', 'B2C3D4E5'),
(34567890, 'Carla Mendes Rocha',    'MATRICULADO', 'C3D4E5F6'),
(45678901, 'Diego Ferreira Neto',   'MATRICULADO', 'D4E5F6G7'),
(56789012, 'Maria Vieira Silva',  'MATRICULADO', 'E5F6G7H8'),
(67890123, 'Felipe Augusto Costa',  'TRANCADO',    NULL);        -- aluno sem tag e trancado, útil para testar casos negativos


-- ------------------------------------------------------------
--  tb_professores
-- ------------------------------------------------------------
INSERT INTO tb_professores (ra_professor, nome_professor) VALUES
(11111111, 'Prof. Ricardo Alves'),
(22222222, 'Profa. Mariana Torres'),
(33333333, 'Prof. Carlos Eduardo Pinto');


-- ------------------------------------------------------------
--  tb_disciplinas
-- ------------------------------------------------------------
INSERT INTO tb_disciplinas (nome_disciplina) VALUES
('Sistemas Embarcados'),
('Redes de Computadores'),
('Engenharia de Software'),
('Banco de Dados'),
('Internet das Coisas');


-- ------------------------------------------------------------
--  tb_salas
-- ------------------------------------------------------------
INSERT INTO tb_salas (numero, bloco, campus, id_dispositivo) VALUES
(1001, 1, 'ASA NORTE', 1001),
(1102, 1, 'ASA NORTE', 1002),
(2301, 2, 'ASA NORTE', 1003),
(2102, 2, 'ASA NORTE', NULL),   -- sala sem dispositivo instalado
(3001, 3, 'ASA NORTE', 1004);


-- ------------------------------------------------------------
--  tb_turmas
--  Considera coluna turno (MATUTINO | VESPERTINO | NOTURNO)
--  no lugar de horario
-- ------------------------------------------------------------
INSERT INTO tb_turmas (id_disciplina, ra_professor, dia_semana, turno, id_sala, semestre_oferta) VALUES
(1, 11111111, 'SEG', 'MATUTINO',    1, '2025.1'),  -- Sistemas Embarcados, sala 101
(2, 22222222, 'TER', 'VESPERTINO',  2, '2025.1'),  -- Redes, sala 102
(3, 33333333, 'QUA', 'NOTURNO',     3, '2025.1'),  -- Eng. Software, sala 201
(4, 11111111, 'QUI', 'MATUTINO',    1, '2025.1'),  -- Banco de Dados, sala 101
(5, 22222222, 'SEX', 'VESPERTINO',  5, '2025.1');  -- IoT, sala 301

-- ------------------------------------------------------------
--  tb_matricula_turma
-- ------------------------------------------------------------
INSERT INTO tb_matricula_turma (ra_aluno, id_turma, data_efetivacao, status_matricula) VALUES
(12345678, 9, '2025-02-01', 'ATIVO'),
(23456789, 9, '2025-02-01', 'ATIVO'),
(34567890, 9, '2025-02-01', 'ATIVO'),
(45678901, 9, '2025-02-01', 'ATIVO'),
(56789012, 9, '2025-02-01', 'ATIVO'),
(12345678, 10, '2025-02-01', 'ATIVO'),  -- Ana também matriculada em Redes
(23456789, 11, '2025-02-01', 'ATIVO'),  -- Bruno também em Eng. Software
(34567890, 13, '2025-02-01', 'ATIVO'),  -- Carla também em IoT
(67890123, 9, '2025-02-01', 'CANCELADO'); -- Felipe trancado — útil para testar matrícula inativa


-- ------------------------------------------------------------
--  tb_aulas
--  Datas fictícias para não depender do dia atual
--  Para testes do fluxo completo, ajuste data_aula para hoje
-- ------------------------------------------------------------
INSERT INTO tb_aulas (id_turma, data_aula, permissao_validar) VALUES
(9, '2025-03-03', 0),  -- aula passada, validação bloqueada
(9, '2025-03-10', 1),  -- aula passada, validação liberada
(10, '2025-03-04', 0),
(11, '2025-03-05', 0),
(13, '2025-03-07', 1);

select * from tb_aulas;
-- ------------------------------------------------------------
--  tb_presenca
--  Registros vinculados às aulas e matrículas acima
-- ------------------------------------------------------------
INSERT INTO tb_presenca (id_aula, id_matricula, situacao_presenca, data_hora_registro, data_hora_validacao) VALUES
(1, 10, 'PRESENTE',           '2025-03-03 07:35:00', '2025-03-03 09:00:00'),
(1, 11, 'PRESENTE',           '2025-03-03 07:36:00', '2025-03-03 09:01:00'),
(1, 12, 'AUSENTE',            '2025-03-03 07:37:00', NULL),
(2, 13, 'VALIDACAO_PENDENTE', '2025-03-10 07:40:00', NULL),
(2, 14, 'PRESENTE',           '2025-03-10 07:41:00', '2025-03-10 09:05:00');
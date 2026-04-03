-- ============================================================
--  SISTEMA DE CONTROLE DE PRESENÇA VIA RFID
--  Trabalho de Conclusão de Curso — Engenharia de Computação
--  MySQL 8.0 | Windows
-- ============================================================

-- ============================================================
--  TABELAS
-- ============================================================

-- ------------------------------------------------------------
--  tb_alunos
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tb_alunos (
    ra_aluno        INT(8)          NOT NULL,
    nome_aluno      VARCHAR(150)    NOT NULL,
    situacao_aluno  ENUM(
                        'MATRICULADO',
                        'TRANCADO',
                        'PRE_MATRICULADO'
                    )               NOT NULL DEFAULT 'PRE_MATRICULADO',
    rfid_uid        VARCHAR(64)     NULL     DEFAULT NULL
                        COMMENT 'UID do cartão/tag RFID do aluno — NULL enquanto não cadastrado',

    CONSTRAINT pk_alunos    PRIMARY KEY (ra_aluno),
    CONSTRAINT uq_rfid_uid  UNIQUE      (rfid_uid)
)
ENGINE  = InnoDB
DEFAULT CHARSET  = utf8mb4
COLLATE = utf8mb4_unicode_ci
COMMENT = 'Cadastro de alunos vinculados ao sistema de presença RFID';


-- ------------------------------------------------------------
--  tb_professores
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tb_professores (
    ra_professor    INT(8)          NOT NULL,
    nome_professor  VARCHAR(150)    NOT NULL,

    CONSTRAINT pk_professores PRIMARY KEY (ra_professor)
)
ENGINE  = InnoDB
DEFAULT CHARSET  = utf8mb4
COLLATE = utf8mb4_unicode_ci
COMMENT = 'Cadastro de professores';


-- ------------------------------------------------------------
--  tb_disciplinas
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tb_disciplinas (
    id_disciplina   INT(3)          NOT NULL AUTO_INCREMENT,
    nome_disciplina VARCHAR(100)    NOT NULL,

    CONSTRAINT pk_disciplinas PRIMARY KEY (id_disciplina)
)
ENGINE  = InnoDB
DEFAULT CHARSET  = utf8mb4
COLLATE = utf8mb4_unicode_ci
COMMENT = 'Catálogo de disciplinas ofertadas';


-- ------------------------------------------------------------
--  tb_salas
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tb_salas (
    id_sala         INT(3)          NOT NULL AUTO_INCREMENT,
    numero          INT(5)          NOT NULL COMMENT 'Número da sala',
    bloco           INT(2)          NOT NULL,
    campus          VARCHAR(10)     NOT NULL,
    id_dispositivo  INT             NULL     DEFAULT NULL
                        COMMENT 'ID do dispositivo RFID instalado na sala',

    CONSTRAINT pk_salas         PRIMARY KEY (id_sala),
    CONSTRAINT uq_dispositivo   UNIQUE      (id_dispositivo)
)
ENGINE  = InnoDB
DEFAULT CHARSET  = utf8mb4
COLLATE = utf8mb4_unicode_ci
COMMENT = 'Salas de aula com dispositivo de verificação de presença instalado';


-- ------------------------------------------------------------
--  tb_turmas
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tb_turmas (
    id_turma        INT             NOT NULL AUTO_INCREMENT,
    id_disciplina   INT(3)          NOT NULL,
    ra_professor    INT(8)          NOT NULL,
    dia_semana      ENUM(
                        'SEG','TER','QUA','QUI','SEX','SAB'
                    )               NOT NULL,
    horario         VARCHAR(11)     NOT NULL COMMENT 'Intervalo no formato HH:MM-HH:MM — ex.: 07:30-09:10',
    id_sala         INT(3)          NOT NULL,
    semestre_oferta CHAR(6)         NOT NULL COMMENT 'Formato: YYYYS — ex.: 2025.1',

    CONSTRAINT pk_turmas        PRIMARY KEY  (id_turma),
    CONSTRAINT fk_turmas_disc   FOREIGN KEY  (id_disciplina)
        REFERENCES tb_disciplinas (id_disciplina)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_turmas_prof   FOREIGN KEY  (ra_professor)
        REFERENCES tb_professores (ra_professor)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_turmas_sala   FOREIGN KEY  (id_sala)
        REFERENCES tb_salas       (id_sala)
        ON UPDATE CASCADE ON DELETE RESTRICT

    -- formato esperado: HH:MM-HH:MM (validado na camada de aplicação)
)
ENGINE  = InnoDB
DEFAULT CHARSET  = utf8mb4
COLLATE = utf8mb4_unicode_ci
COMMENT = 'Turmas ofertadas por semestre, vinculadas a sala, professor e disciplina';

CREATE INDEX idx_turmas_disciplina  ON tb_turmas (id_disciplina);
CREATE INDEX idx_turmas_professor   ON tb_turmas (ra_professor);
CREATE INDEX idx_turmas_sala        ON tb_turmas (id_sala);
CREATE INDEX idx_turmas_semestre    ON tb_turmas (semestre_oferta);


-- ------------------------------------------------------------
--  tb_aulas
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tb_aulas (
    id_aula             INT             NOT NULL AUTO_INCREMENT,
    id_turma            INT             NOT NULL,
    data_aula           DATE            NOT NULL,
    permissao_validar   TINYINT(1)      NOT NULL DEFAULT 0
                            COMMENT '0 = bloqueado | 1 = validação liberada pelo professor',

    CONSTRAINT pk_aulas         PRIMARY KEY (id_aula),
    CONSTRAINT fk_aulas_turma   FOREIGN KEY (id_turma)
        REFERENCES tb_turmas (id_turma)
        ON UPDATE CASCADE ON DELETE RESTRICT,

    -- evita aula duplicada para a mesma turma no mesmo dia
    CONSTRAINT uq_aula_turma_data UNIQUE (id_turma, data_aula)
)
ENGINE  = InnoDB
DEFAULT CHARSET  = utf8mb4
COLLATE = utf8mb4_unicode_ci
COMMENT = 'Registro de cada aula realizada por turma';

CREATE INDEX idx_aulas_data ON tb_aulas (data_aula);


-- ------------------------------------------------------------
--  tb_matriculas
-- ------------------------------------------------------------
--  Criada ANTES de tb_presenca para satisfazer a FK referenciada nela.
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tb_matricula_turma (
    id_matricula_turma  INT             NOT NULL AUTO_INCREMENT,
    ra_aluno            INT(8)          NOT NULL,
    id_turma            INT             NOT NULL,
    data_efetivacao     DATE            NOT NULL DEFAULT (CURRENT_DATE),
    status_matricula    ENUM(
                            'ATIVO',
                            'CANCELADO',
                            'TRANCADO',
                            'CONCLUIDO'
                        )               NOT NULL DEFAULT 'ATIVO',

    CONSTRAINT pk_matricula_turma        PRIMARY KEY (id_matricula_turma),
    CONSTRAINT fk_mat_aluno         FOREIGN KEY (ra_aluno)
        REFERENCES tb_alunos  (ra_aluno)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_mat_turma         FOREIGN KEY (id_turma)
        REFERENCES tb_turmas  (id_turma)
        ON UPDATE CASCADE ON DELETE RESTRICT,

    -- um aluno não pode estar matriculado duas vezes na mesma turma
    CONSTRAINT uq_matricula_aluno_turma UNIQUE (ra_aluno, id_turma)
)
ENGINE  = InnoDB
DEFAULT CHARSET  = utf8mb4
COLLATE = utf8mb4_unicode_ci
COMMENT = 'Matrículas dos alunos nas turmas de cada semestre';

CREATE INDEX idx_mat_aluno  ON tb_matricula_turma (ra_aluno);
CREATE INDEX idx_mat_turma  ON tb_matricula_turma (id_turma);
CREATE INDEX idx_mat_status ON tb_matricula_turma (status_matricula);


-- ------------------------------------------------------------
--  tb_presenca
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tb_presenca (
    id_presenca             INT             NOT NULL AUTO_INCREMENT,
    id_aula                 INT             NOT NULL,
    id_matricula            INT             NOT NULL
                                COMMENT 'FK para tb_matriculas — identifica aluno + turma',
    situacao_presenca       ENUM(
                                'VALIDACAO_PENDENTE',
                                'PRESENTE',
                                'AUSENTE',
                                'JUSTIFICADO'
                            )               NOT NULL DEFAULT 'VALIDACAO_PENDENTE',
    data_hora_registro      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP
                                COMMENT 'Momento da leitura RFID',
    data_hora_validacao     DATETIME        NULL     DEFAULT NULL
                                COMMENT 'Momento em que o aluno validou a presença',

    CONSTRAINT pk_presenca          PRIMARY KEY (id_presenca),
    CONSTRAINT fk_pres_aula         FOREIGN KEY (id_aula)
        REFERENCES tb_aulas     (id_aula)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_pres_matricula    FOREIGN KEY (id_matricula)
        REFERENCES tb_matriculas (id_matricula)
        ON UPDATE CASCADE ON DELETE RESTRICT,

    -- evita registro duplicado do mesmo aluno na mesma aula
    CONSTRAINT uq_presenca_aula_matricula UNIQUE (id_aula, id_matricula)
)
ENGINE  = InnoDB
DEFAULT CHARSET  = utf8mb4
COLLATE = utf8mb4_unicode_ci
COMMENT = 'Registros de presença capturados via RFID e validados pelo professor';

CREATE INDEX idx_pres_aula          ON tb_presenca (id_aula);
CREATE INDEX idx_pres_matricula     ON tb_presenca (id_matricula);
CREATE INDEX idx_pres_situacao      ON tb_presenca (situacao_presenca);
CREATE INDEX idx_pres_dt_registro   ON tb_presenca (data_hora_registro);


-- ============================================================
--  REATIVA VERIFICAÇÃO DE CHAVES ESTRANGEIRAS
-- ============================================================
SET FOREIGN_KEY_CHECKS = 1;

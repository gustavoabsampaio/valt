CREATE TABLE usuario (
    id_usuario  SERIAL      PRIMARY KEY,
    cpf         VARCHAR(11) UNIQUE NOT NULL,
    email       VARCHAR(255) UNIQUE NOT NULL,
    nome        VARCHAR(30) NOT NULL,
    sobrenome   VARCHAR(30) NOT NULL,
    nickname    VARCHAR(30) UNIQUE,
    nascimento  DATE        NOT NULL
);
CREATE TABLE loja (
    id_loja     SERIAL      PRIMARY KEY,
    cpfcnpj     VARCHAR(14)     UNIQUE,
    nome        VARCHAR(50) NOT NULL,
    email       VARCHAR(255) UNIQUE NOT NULL,
    telefone    VARCHAR(15),
    logo_url    VARCHAR(255)
);

CREATE TABLE peca (
    id_peca     SERIAL              PRIMARY KEY,
    id_loja     INTEGER             NOT NULL,
    nome        VARCHAR(50)         NOT NULL,
    preco       DECIMAL(10,2)       NOT NULL,
    descricao   TEXT,
    disponivel  BOOLEAN             NOT NULL DEFAULT TRUE,
    promocao    INTEGER REFERENCES promocao(id_promocao) NULL,
    colecao     VARCHAR(50),
    ano         SMALLINT,
    CONSTRAINT fk_peca_loja
        FOREIGN KEY(id_loja)
            REFERENCES loja(id_loja),
    CONSTRAINT fk_peca_promocao
        FOREIGN KEY(promocao)
            REFERENCES promocao(id_promocao)
);


CREATE TABLE promocao (
    id_promocao         SERIAL         PRIMARY KEY,
    id_loja             INTEGER        NOT NULL,
    id_peca             INTEGER        NOT NULL,
    data_inicio         TIMESTAMP      NOT NULL,
    data_fim            TIMESTAMP      NOT NULL,
    preco_promocao      DECIMAL(10,2)  NOT NULL,
    porcent_desconto    INTEGER        NOT NULL,
    CONSTRAINT fk_promocao_loja
        FOREIGN KEY(id_loja)
            REFERENCES loja(id_loja),
    CONSTRAINT fk_promocao_peca
        FOREIGN KEY(id_peca)
            REFERENCES peca(id_peca)
);


CREATE TABLE material (
    id_material SERIAL      PRIMARY KEY,
    nome        VARCHAR(30) UNIQUE NOT NULL,
    id_peca     INTEGER     NOT NULL,
    id_loja     INTEGER     NOT NULL,
    CONSTRAINT fk_material_peca
	FOREIGN KEY(id_peca)
		REFERENCES peca(id_peca),
    CONSTRAINT fk_material_loja
	FOREIGN KEY(id_loja)
		REFERENCES loja(id_loja)
);



CREATE TABLE segue (
    id_usuario      INTEGER,
    id_loja         INTEGER,
    data_seguiu     DATE        NOT NULL,
    PRIMARY KEY (id_usuario, id_loja),
    CONSTRAINT fk_segue_loja
        FOREIGN KEY(id_loja)
            REFERENCES loja(id_loja),
    CONSTRAINT fk_segue_usuario
        FOREIGN KEY(id_usuario)
            REFERENCES usuario(id_usuario)
);

CREATE TABLE favorita (
    id_usuario      INTEGER,
    id_peca         INTEGER,
    data_adicao     DATE        NOT NULL,
    preco_adicao    FLOAT       NOT NULL
    PRIMARY KEY (id_usuario, id_peca),
    CONSTRAINT fk_favorita_peca
        FOREIGN KEY(id_peca)
            REFERENCES peca(id_peca),
    CONSTRAINT fk_favorita_usuario
        FOREIGN KEY(id_usuario)
            REFERENCES usuario(id_usuario)
);

CREATE TABLE estilo (
    id_estilo   SERIAL      PRIMARY KEY,
    nome        VARCHAR(50) NOT NULL,
    descricao   TEXT        NOT NULL
);

CREATE TABLE procura (
    id_usuario  INTEGER     NOT NULL,
    id_estilo   INTEGER     NOT NULL,
    data_ini    DATE        NOT NULL,
    data_fim    DATE,
    CONSTRAINT fk_procura_usuario
        FOREIGN KEY(id_usuario)
            REFERENCES usuario(id_usuario),
    CONSTRAINT fk_procura_estilo
        FOREIGN KEY(id_estilo)
            REFERENCES estilo(id_estilo)
);

CREATE TABLE estilo_peca (
    id_peca         INTEGER     NOT NULL,
    id_estilo       INTEGER     NOT NULL,
    caracteristica  TEXT,
    CONSTRAINT fk_estilo_peca_peca
        FOREIGN KEY(id_peca)
            REFERENCES peca(id_peca),
    CONSTRAINT fk_estilo_peca_estilo
        FOREIGN KEY(id_estilo)
            REFERENCES estilo(id_estilo)
    PRIMARY KEY (id_peca, id_estilo)
);

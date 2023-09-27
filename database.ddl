-- estilos serão mapeados por bits, cada bit um estilo
CREATE TABLE usuario (
    cpf         INTEGER     PRIMARY KEY,
    email       VARCHAR(30) UNIQUE NOT NULL,
    nascimento  DATE        NOT NULL,
    estilos     BIT(10)     NOT NULL 
);

CREATE TABLE loja (
    cpfcnpj     INTEGER     PRIMARY KEY,
    nome        VARCHAR(25) NOT NULL,
    email       VARCHAR(30) UNIQUE NOT NULL,
    telefone    INTEGER,
    logo        BYTEA,
    estilos     BIT(10)     NOT NULL
);

CREATE TABLE peca (
    id          INTEGER     PRIMARY KEY,
    id_loja     INTEGER     NOT NULL,
    nome        VARCHAR(30) NOT NULL,
    preco       FLOAT       NOT NULL,
    descricao   TEXT,
    materiais   BIT(10)     NOT NULL,
    disponivel  BOOLEAN     NOT NULL,
    promocao    INTEGER,
    estilos     BIT(10)     NOT NULL,
    colecao     VARCHAR(20),
    ano         SMALLINT,
    CONSTRAINT fk_peca_loja
        FOREIGN KEY(id_loja)
            REFERENCES loja(cpfcnpj),
    CONSTRAINT fk_peca_promocao
        FOREIGN KEY(promocao)
            REFERENCES promocao(id)
);

CREATE TABLE promocao (
    id                  INTEGER     PRIMARY KEY,
    id_loja             INTEGER     NOT NULL,
    id_peca             INTEGER     NOT NULL,
    data_inicio         DATETIME    NOT NULL,
    data_fim            DATETIME    NOT NULL,
    preco_promocao      FLOAT       NOT NULL,
    porcent_desconto    INTEGER     NOT NULL,
    CONSTRAINT fk_promocao_loja
        FOREIGN KEY(id_loja)
            REFERENCES loja(cpfcnpj),
    CONSTRAINT fk_promocao_peca
        FOREIGN KEY(id_peca)
            REFERENCES peca(id)
);

CREATE TABLE segue (
    id_usuario      INTEGER,
    id_loja         INTEGER,
    data_seguiu     DATE        NOT NULL,
    PRIMARY KEY (id_usuario, id_loja),
    CONSTRAINT fk_segue_loja
        FOREIGN KEY(id_loja)
            REFERENCES loja(cpfcnpj),
    CONSTRAINT fk_segue_usuario
        FOREIGN KEY(id_usuario)
            REFERENCES usuario(cpf)
);

CREATE TABLE favorita (
    id_usuario      INTEGER,
    id_peca         INTEGER,
    data_adicao     DATE        NOT NULL,
    preco_adicao    FLOAT       NOT NULL
    PRIMARY KEY (id_usuario, id_peca),
    CONSTRAINT fk_favorita_peca
        FOREIGN KEY(id_peca)
            REFERENCES peca(id),
    CONSTRAINT fk_favorita_usuario
        FOREIGN KEY(id_usuario)
            REFERENCES usuario(cpf)
);
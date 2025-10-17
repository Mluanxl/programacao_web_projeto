CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    telefone VARCHAR(11),
    instituicao VARCHAR(50),
    usuario_login VARCHAR(25) UNIQUE NOT NULL,
    senha VARCHAR(25) NOT NULL,
    perfil VARCHAR(15) CHECK (perfil IN ('aluno', 'professor', 'organizador'))
);

CREATE TABLE evento (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    tipo VARCHAR(20) CHECK (tipo IN ('seminario', 'palestra', 'monitoria')),
    titulo VARCHAR(50) NOT NULL,
    data_inicio DATE,
    data_fim DATE,
    local VARCHAR(50),
    capacidade INTEGER,
    organizador_id INTEGER,
    FOREIGN KEY (organizador_id) REFERENCES usuario(id)
);

CREATE TABLE inscricao (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    usuario_id INTEGER,
    evento_id INTEGER,
    data_inscricao DATETIME,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id),
    FOREIGN KEY (evento_id) REFERENCES evento(id)
);

CREATE TABLE certificado (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    inscricao_id INTEGER,
    codigo VARCHAR(10) UNIQUE,
    emissao DATETIME,
    FOREIGN KEY (inscricao_id) REFERENCES inscricao(id)
);

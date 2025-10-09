-- Tabela de turmas
CREATE TABLE turmas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    ano_letivo YEAR NOT NULL,
    turno ENUM('manha', 'tarde', 'noite') NOT NULL
);

-- Tabela de professores_turmas (relação muitos-para-muitos)
CREATE TABLE professores_turmas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    professor_id INT,
    turma_id INT,
    disciplina VARCHAR(50) NOT NULL,
    FOREIGN KEY (professor_id) REFERENCES professores(id),
    FOREIGN KEY (turma_id) REFERENCES turmas(id)
);

-- Tabela de alunos_turmas
CREATE TABLE alunos_turmas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    aluno_id INT,
    turma_id INT,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id),
    FOREIGN KEY (turma_id) REFERENCES turmas(id)
);

-- Tabela de faltas
CREATE TABLE faltas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    aluno_id INT,
    turma_id INT,
    data_falta DATE NOT NULL,
    justificada BOOLEAN DEFAULT FALSE,
    observacao TEXT,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id),
    FOREIGN KEY (turma_id) REFERENCES turmas(id)
);

-- Tabela de resumos de aula
CREATE TABLE resumos_aula (
    id INT AUTO_INCREMENT PRIMARY KEY,
    professor_id INT,
    turma_id INT,
    unidade INT NOT NULL,
    titulo VARCHAR(200) NOT NULL,
    conteudo TEXT NOT NULL,
    data_publicacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (professor_id) REFERENCES professores(id),
    FOREIGN KEY (turma_id) REFERENCES turmas(id)
);

-- Inserir dados de exemplo
INSERT INTO turmas (nome, ano_letivo, turno) VALUES 
('9º Ano A', 2025, 'manha'),
('9º Ano B', 2025, 'tarde'),
('1º Ano EM', 2025, 'manha');

INSERT INTO professores_turmas (professor_id, turma_id, disciplina) VALUES
(1, 1, 'Matemática'),
(1, 2, 'Matemática'),
(2, 1, 'Português');

INSERT INTO alunos_turmas (aluno_id, turma_id) VALUES
(1, 1);
-- Criação da tabela
CREATE TABLE IF NOT EXISTS public.usuario
(
    id serial PRIMARY KEY,
    nome text NOT NULL,
    senha text,
    cpf character varying(11),
    tipo bigint NOT NULL,
    created_at timestamp,
    updated_at timestamp,
    deleted_at timestamp
);

-- Inserção de dados

INSERT INTO public.usuario (nome, senha, cpf, tipo, created_at, updated_at, deleted_at)
VALUES ('exemplo', 'rae', 123, 20200101, current_timestamp, current_timestamp, NULL);
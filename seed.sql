-- Criação da tabela
CREATE TABLE IF NOT EXISTS public.usuario
(
    id text DEFAULT gen_random_uuid()::text PRIMARY KEY,
    nome text NOT NULL,
    senha text,
    cpf character varying(11),
    tipo character varying(10) NOT NULL, -- admin, cliente
    created_at timestamp,
    updated_at timestamp,
    deleted_at timestamp
);

-- Inserção de dados

INSERT INTO public.usuario (nome, senha, cpf, tipo, created_at, updated_at, deleted_at)
VALUES ('Cliente Pedro', '123', '11122233344', 'cliente', current_timestamp, current_timestamp, NULL);

INSERT INTO public.usuario (nome, senha, cpf, tipo, created_at, updated_at, deleted_at)
VALUES ('Usuário Admin', 'admin', NULL, 'admin', current_timestamp, current_timestamp, NULL);
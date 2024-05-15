-- Criação da tabela de usuários
CREATE TABLE IF NOT EXISTS public.usuario (
    id serial4 NOT NULL PRIMARY KEY,
    nome text NOT NULL,
    email text,
    senha text,
    cpf character varying(11) UNIQUE, -- Adicionando restrição única para a coluna CPF
    tipo character varying(10) NOT NULL,
    created_at timestamp DEFAULT current_timestamp NOT NULL,
    updated_at timestamp,
    deleted_at timestamp
);

-- Criação da tabela de produtos

-- Criação da tabela de pedidos


-- Upsert para tabela de usuários
INSERT INTO public.usuario (nome, senha, cpf, tipo, updated_at, deleted_at, email)
VALUES 
    ('Cliente Pedro', 'senha123', '24945805016', 'cliente', current_timestamp, NULL, 'pedro@email.com'),
    ('Admin Joao',    'senha123', '40986296074', 'admin',   current_timestamp, NULL, 'joao@email.com')
ON CONFLICT (cpf) DO UPDATE
SET 
    nome = EXCLUDED.nome,
    senha = EXCLUDED.senha,
    tipo = EXCLUDED.tipo,
    updated_at = EXCLUDED.updated_at,
    deleted_at = EXCLUDED.deleted_at,
    email = EXCLUDED.email;

-- Upsert para tabela de produtos


-- Upsert para tabela de pedidos

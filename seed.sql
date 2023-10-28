-- Criação da tabela
CREATE TABLE IF NOT EXISTS public.usuario (
    id text DEFAULT gen_random_uuid()::text PRIMARY KEY,
    nome text NOT NULL,
    senha text,
    cpf character varying(11),
    tipo character varying(10) NOT NULL,
    created_at timestamp DEFAULT current_timestamp NOT NULL,
    updated_at timestamp,
    deleted_at timestamp
);

CREATE TABLE IF NOT EXISTS public.produto (
	nome varchar NOT NULL,
	preco float8 NOT NULL,
	imagens varchar NOT NULL,
	categoria varchar NOT NULL,
	id serial4 NOT NULL,
	created_at timestamp DEFAULT current_timestamp NOT NULL,
	updated_at timestamp NULL,
	deleted_at timestamp NULL
);

CREATE TABLE IF NOT EXISTS public.pedido (
	produtos json[] NULL,
	data_mudanca_status timestamp NULL,
	valor float8 NOT NULL,
	status_pedido varchar NULL,
	status_pagamento varchar NULL,
	id text DEFAULT gen_random_uuid()::text PRIMARY KEY,
	created_at timestamp DEFAULT current_timestamp NOT NULL,
	updated_at timestamp NULL,
	deleted_at timestamp NULL
);

-- Inserção de dados
INSERT INTO public.usuario (nome, senha, cpf, tipo, updated_at, deleted_at)
VALUES 
    ('Cliente Pedro', 'senha123', '24945805016', 'cliente', current_timestamp, NULL),
    ('Admin Joao',    'senha123', '40986296074', 'admin',   current_timestamp, NULL);

INSERT INTO public.produto (id, nome, preco, imagens, categoria)
VALUES 
    (1, 'X-Burger',      10.99, 'pth/to/file.png', 'Lanche'),
    (2, 'X-Egg-Burger',  10.99, 'pth/to/file.png', 'Lanche'),
    (3, 'Batata Media',  10.99, 'pth/to/file.png', 'Acompanhamento'),
    (4, 'Batata Grande', 10.99, 'pth/to/file.png', 'Acompanhamento'),
    (5, 'Refrigerante',  10.99, 'pth/to/file.png', 'Bebida'),
    (6, 'Suco',          10.99, 'pth/to/file.png', 'Bebida'),
    (7, 'Sorvete',       10.99, 'pth/to/file.png', 'Sobremesa'),
    (8, 'Cookies',       10.99, 'pth/to/file.png', 'Sobremesa');


INSERT INTO public.pedido (status_pedido, status_pagamento, valor, data_mudanca_status, produtos)
VALUES
    ('Recebido',   'Efetuado', 10.99, current_timestamp, ARRAY ['{"nome": "X-Burger", "quantidade": 1, "valor": 10.99}'::json]),
    ('Pronto',     'Efetuado', 10.99, current_timestamp, ARRAY ['{"nome": "Refrigerante", "quantidade": 1, "valor": 10.99}'::json]),
    ('Finalizado', 'Efetuado', 21.98, current_timestamp, ARRAY ['{"nome": "X-Burger", "quantidade": 1, "valor": 10.99}'::json,'{"nome": "Batata Media", "quantidade": 1, "valor": 10.99}'::json]);


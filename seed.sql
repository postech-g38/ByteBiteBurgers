-- Criação da tabela
CREATE TABLE IF NOT EXISTS public.usuario (
    id serial4 NOT NULL PRIMARY KEY,
    nome text NOT NULL,
    email text,
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
	id serial4 NOT NULL PRIMARY KEY,
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
    pagamento_id varchar NULL,
	id serial4 NOT NULL PRIMARY KEY,
	created_at timestamp DEFAULT current_timestamp NOT NULL,
	updated_at timestamp NULL,
	deleted_at timestamp NULL
);

-- Inserção de dados
INSERT INTO public.usuario (nome, senha, cpf, tipo, updated_at, deleted_at)
VALUES 
    ('Cliente Pedro', 'senha123', '24945805016', 'cliente', current_timestamp, NULL),
    ('Admin Joao',    'senha123', '40986296074', 'admin',   current_timestamp, NULL);

INSERT INTO public.produto (nome, preco, imagens, categoria)
VALUES 
    ('X-Burger',      10.99, 'pth/to/file.png', 'Lanche'),
    ('X-Egg-Burger',  10.99, 'pth/to/file.png', 'Lanche'),
    ('Batata Media',  10.99, 'pth/to/file.png', 'Acompanhamento'),
    ('Batata Grande', 10.99, 'pth/to/file.png', 'Acompanhamento'),
    ('Refrigerante',  10.99, 'pth/to/file.png', 'Bebida'),
    ('Suco',          10.99, 'pth/to/file.png', 'Bebida'),
    ('Sorvete',       10.99, 'pth/to/file.png', 'Sobremesa'),
    ('Cookies',       10.99, 'pth/to/file.png', 'Sobremesa');


INSERT INTO public.pedido (status_pedido, status_pagamento, valor, data_mudanca_status, produtos)
VALUES
    ('Recebido',   'Efetuado', 10.99, current_timestamp, ARRAY ['{"produto_id": 1, "quantidade": 1}'::json]),
    ('Pronto',     'Efetuado', 10.99, current_timestamp, ARRAY ['{"produto_id": 5, "quantidade": 1}'::json]),
    ('Finalizado', 'Efetuado', 21.98, current_timestamp, ARRAY ['{"produto_id": 1, "quantidade": 1}'::json,'{"produto_id": 5, "quantidade": 1}'::json]);

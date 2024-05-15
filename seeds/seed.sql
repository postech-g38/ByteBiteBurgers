


-- Criação da tabela de produtos
CREATE TABLE IF NOT EXISTS public.produto (
    nome varchar NOT NULL UNIQUE, -- Adicionando restrição única para a coluna nome
    preco float8 NOT NULL,
    imagens varchar NOT NULL,
    categoria varchar NOT NULL,
    id serial4 NOT NULL PRIMARY KEY,
    created_at timestamp DEFAULT current_timestamp NOT NULL,
    updated_at timestamp NULL,
    deleted_at timestamp NULL
);

-- Criação da tabela de pedidos
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


-- Upsert para tabela de produtos
INSERT INTO public.produto (nome, preco, imagens, categoria)
VALUES 
    ('X-Burger',      10.99, 'pth/to/file.png', 'Lanche'),
    ('X-Egg-Burger',  10.99, 'pth/to/file.png', 'Lanche'),
    ('Batata Media',  10.99, 'pth/to/file.png', 'Acompanhamento'),
    ('Batata Grande', 10.99, 'pth/to/file.png', 'Acompanhamento'),
    ('Refrigerante',  10.99, 'pth/to/file.png', 'Bebida'),
    ('Suco',          10.99, 'pth/to/file.png', 'Bebida'),
    ('Sorvete',       10.99, 'pth/to/file.png', 'Sobremesa'),
    ('Cookies',       10.99, 'pth/to/file.png', 'Sobremesa')
ON CONFLICT (nome) DO NOTHING;

-- Upsert para tabela de pedidos
INSERT INTO public.pedido (status_pedido, status_pagamento, valor, data_mudanca_status, produtos)
VALUES
    ('Pronto',     'Efetuado', 10.99, current_timestamp, ARRAY ['{"produto_id": 5, "quantidade": 1}'::json]),
    ('Pronto',     'Efetuado', 10.99, current_timestamp - INTERVAL '10 min', ARRAY ['{"produto_id": 4, "quantidade": 2}'::json]),
    ('Em preparação', 'Efetuado', 10.99, current_timestamp, ARRAY ['{"produto_id": 3, "quantidade": 3}'::json]),
    ('Em preparação', 'Efetuado', 10.99, current_timestamp - INTERVAL '10 min', ARRAY ['{"produto_id": 1, "quantidade": 4}'::json]),
    ('Recebido',   'Efetuado', 10.99, current_timestamp, ARRAY ['{"produto_id": 1, "quantidade": 1}'::json]),
    ('Recebido',   'Efetuado', 10.99, current_timestamp - INTERVAL '10 min', ARRAY ['{"produto_id": 1, "quantidade": 1}'::json]),
    ('Finalizado', 'Efetuado', 21.98, current_timestamp, ARRAY ['{"produto_id": 1, "quantidade": 1}'::json,'{"produto_id": 5, "quantidade": 1}'::json])
ON CONFLICT DO NOTHING;
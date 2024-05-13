-- Criação da tabela de usuários

-- Criação da tabela de pedidos
CREATE TABLE IF NOT EXISTS public.pagamento (
    pedido_id int NULL,
    usuario_id timestamp NULL,
    valor float8 NOT NULL,
    metodo varchar NULL,
    status varchar NULL,
    id serial4 NOT NULL PRIMARY KEY,
    created_at timestamp DEFAULT current_timestamp NOT NULL,
    updated_at timestamp NULL,
);

-- Upsert para tabela de usuários
-- INSERT INTO public.usuario (nome, senha, cpf, tipo, updated_at, deleted_at, email)
-- VALUES 
--     ('Cliente Pedro', 'senha123', '24945805016', 'cliente', current_timestamp, NULL, 'pedro@email.com'),
--     ('Admin Joao',    'senha123', '40986296074', 'admin',   current_timestamp, NULL, 'joao@email.com')
-- ON CONFLICT (cpf) DO UPDATE
-- SET 
--     nome = EXCLUDED.nome,
--     senha = EXCLUDED.senha,
--     tipo = EXCLUDED.tipo,
--     updated_at = EXCLUDED.updated_at,
--     deleted_at = EXCLUDED.deleted_at,
--     email = EXCLUDED.email;

-- -- Upsert para tabela de produtos
-- INSERT INTO public.produto (nome, preco, imagens, categoria)
-- VALUES 
--     ('X-Burger',      10.99, 'pth/to/file.png', 'Lanche'),
--     ('X-Egg-Burger',  10.99, 'pth/to/file.png', 'Lanche'),
--     ('Batata Media',  10.99, 'pth/to/file.png', 'Acompanhamento'),
--     ('Batata Grande', 10.99, 'pth/to/file.png', 'Acompanhamento'),
--     ('Refrigerante',  10.99, 'pth/to/file.png', 'Bebida'),
--     ('Suco',          10.99, 'pth/to/file.png', 'Bebida'),
--     ('Sorvete',       10.99, 'pth/to/file.png', 'Sobremesa'),
--     ('Cookies',       10.99, 'pth/to/file.png', 'Sobremesa')
-- ON CONFLICT (nome) DO NOTHING;

-- -- Upsert para tabela de pedidos
-- INSERT INTO public.pedido (status_pedido, status_pagamento, valor, data_mudanca_status, produtos)
-- VALUES
--     ('Pronto',     'Efetuado', 10.99, current_timestamp, ARRAY ['{"produto_id": 5, "quantidade": 1}'::json]),
--     ('Pronto',     'Efetuado', 10.99, current_timestamp - INTERVAL '10 min', ARRAY ['{"produto_id": 4, "quantidade": 2}'::json]),
--     ('Em preparação', 'Efetuado', 10.99, current_timestamp, ARRAY ['{"produto_id": 3, "quantidade": 3}'::json]),
--     ('Em preparação', 'Efetuado', 10.99, current_timestamp - INTERVAL '10 min', ARRAY ['{"produto_id": 1, "quantidade": 4}'::json]),
--     ('Recebido',   'Efetuado', 10.99, current_timestamp, ARRAY ['{"produto_id": 1, "quantidade": 1}'::json]),
--     ('Recebido',   'Efetuado', 10.99, current_timestamp - INTERVAL '10 min', ARRAY ['{"produto_id": 1, "quantidade": 1}'::json]),
--     ('Finalizado', 'Efetuado', 21.98, current_timestamp, ARRAY ['{"produto_id": 1, "quantidade": 1}'::json,'{"produto_id": 5, "quantidade": 1}'::json])
-- ON CONFLICT DO NOTHING;
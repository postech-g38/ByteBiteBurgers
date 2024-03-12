import logging

from contextlib import contextmanager


from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import Session
from sqlalchemy import text

from src.settings import  get_settings
from src.adapters.database.models.base_model import BaseModel


_logger = logging.getLogger(__name__)


def _create_sync_engine():
    return create_engine(
        url=get_settings().database_settings.unittest_sync_uri,
        pool_size=10, #  get_settings().database.database_pool_size,
        max_overflow=20, #  get_settings().database.database_max_overflow,
        pool_pre_ping=True,
        pool_recycle=3600, #  get_settings().database.database_pool_timeout_seconds,
        echo=True,  #get_settings().database.database_echo
    )


sync_engine = _create_sync_engine()

SyncSessionLocal = sessionmaker(
    bind=sync_engine, 
    class_=Session, 
    autoflush=False, 
    autocommit=False, 
    expire_on_commit=False, 
    future=True)


@contextmanager
def get_session() -> Session:
    _sync_scoped_session: scoped_session = scoped_session(session_factory=SyncSessionLocal)
    try:
        yield _sync_scoped_session()
        _sync_scoped_session.commit()
    except Exception as ex:
        _sync_scoped_session.rollback()
        raise
    finally:
        _sync_scoped_session.remove()


@contextmanager
def get_connection():
    with sync_engine.connect() as connection:
        with connection.begin():
            yield connection


def run_migrations():
    BaseModel.metadata.create_all(bind=sync_engine, checkfirst=True)


def add_seed():
    with get_connection as conn:
        conn.execute(text("""
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
            """)
        )
from enum import Enum


class UsuarioTipo(Enum):
    CLIENTE: str = 'cliente'
    ADMIN:   str = 'admin'


class PedidoStatus(Enum):
    RECEBIDO:      str = 'Recebido'
    EM_PREPARACAO: str = 'Em preparação'
    PRONTO:        str = 'Pronto'
    FINALIZADO:    str = 'Finalizado'


class ProdutoCategorias(Enum):
    LANCHE:         str = 'Lanche'
    ACOMPANHAMENTO: str = 'Acompanhamento'
    BEBIDA:         str = 'Bebida'
    SOBREMESA:      str = 'Sobremesa'

from enum import Enum


class UsuarioTipo(str, Enum):
    CLIENTE: str = 'cliente'
    ADMIN:   str = 'admin'


class PedidoStatus(str, Enum):
    RECEBIDO:      str = 'Recebido'
    EM_PREPARACAO: str = 'Em preparação'
    PRONTO:        str = 'Pronto'
    FINALIZADO:    str = 'Finalizado'


class ProdutoCategorias(str, Enum):
    LANCHE:         str = 'Lanche'
    ACOMPANHAMENTO: str = 'Acompanhamento'
    BEBIDA:         str = 'Bebida'
    SOBREMESA:      str = 'Sobremesa'

from enum import Enum


class PedidoStatus(Enum):
    RECEBIDO:      str = 'Recebido'
    EM_PREPARACAO: str = 'Em preparação'
    PRONTO:        str = 'Pronto'
    FINALIZADO:    str = 'Finalizado'

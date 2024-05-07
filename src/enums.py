from enum import Enum


class PagamentoStatus(Enum):
    CRIADO = 'criado'
    APROVADO = 'aprovado'
    NEGADO = 'negado'
    CANCELADO = 'cancelado'

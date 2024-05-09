from enum import Enum


class PagamentoStatus(str, Enum):
    CRIADO = 'criado'
    APROVADO = 'aprovado'
    NEGADO = 'negado'
    CANCELADO = 'cancelado'


class PagamentoMethod(str, Enum):
    CARTAO_CREDITO = 'cartao_credito'
    CARTAO_DEBITO = 'cartao_debito'
    DINHEIRO = 'dinheiro'
    PIX = 'pix'
    
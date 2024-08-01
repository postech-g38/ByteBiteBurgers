from datetime import datetime


PAGAMENTO_CRIADO_PAYLOAD = {
    'pedido_id': 1,
    'usuario_id': 1,
    'valor': 10.00,
    'metodo': 'cartao_credito',
    'status': 'aprovado'
}


PAGAMENTO_CRIADO_MODEL = {
    'id': 1,
    'created_at': datetime.now(),
    'updated_at': None,
    'pedido_id': 1,
    'usuario_id': 1,
    'valor': 10.00,
    'metodo': 'cartao_credito',
    'status': 'aprovado'
}


PAGAMENTO_APROVADO_MODEL = {
    'id': 2,
    'created_at': datetime.now(),
    'updated_at': None,
    'pedido_id': 1,
    'usuario_id': 1,
    'valor': 10.00,
    'metodo': 'cartao_credito',
    'status': 'aprovado'
}
from datetime import datetime


PEDIDO_MODEL_LANCHE_MOCK = {
    'id': '1',
    'created_at': datetime.now(),
    'updated_at': datetime.now(),
    'deleted_at': datetime.now(),
    'valor': 10.99,
    'produtos': [
        {'produto': 'X-Burger', 'quantidade': 1, 'valor': 10.99}
    ],
    'status_pedido': 'Recebido',
    'status_pagamento': 'Efetuado'
}


PEDIDO_MODEL_REFRIGERANTE_MOCK = {
    'id': '2',
    'created_at': datetime.now(),
    'updated_at': datetime.now(),
    'deleted_at': datetime.now(),
    'valor': 10.99,
    'produtos': [
        {'produto': 'Refrigerante', 'quantidade': 1, 'valor': 10.99}
    ],
    'status_pedido': 'Pronto',
    'status_pagamento': 'Efetuado'
}


PEDIDO_MODEL_COMBO_MOCK = {
    'id': '3',
    'created_at': datetime.now(),
    'updated_at': datetime.now(),
    'deleted_at': datetime.now(),
    'valor': 21.98,
    'produtos': [
        {'produto': 'X-Burger',     'quantidade': 1, 'valor': 10.99},
        {'produto': 'Batata Media', 'quantidade': 1, 'valor': 10.99}
    ],
    'status_pedido': 'Finalizado',
    'status_pagamento': 'Efetuado'
}
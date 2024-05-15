from datetime import datetime
import json


PEDIDO_MODEL_LANCHE_MOCK = {
    'valor': 10.99,
    'produtos': json.dumps({
        'data': [
            {'produto_id': 1, 'quantidade': 1}
        ]
    }),
    'status_pedido': 'Recebido',
    'status_pagamento': 'Efetuado',
    'pagamento_id': 'abc'
}


PEDIDO_MODEL_REFRIGERANTE_MOCK = {
    'valor': 10.99,
    'produtos': json.dumps({
        'data': [
            {'produto_id': 5, 'quantidade': 1}
        ]
    }),
    'status_pedido': 'Pronto',
    'status_pagamento': 'Efetuado',
    'pagamento_id': 'abc'
}


PEDIDO_MODEL_COMBO_MOCK = {
    'valor': 21.98,
    'produtos': json.dumps({
        'data': [
            {'produto_id': 1, 'quantidade': 1}, 
            {'produto_id': 5, 'quantidade': 1}
        ]
    }),
    'status_pedido': 'Finalizado',
    'status_pagamento': 'Efetuado',
    'pagamento_id': 'abc'
}

PEDIDO_MODEL_COMBO_MAKING_MOCK = {
    'valor': 21.98,
    'produtos': json.dumps({
        'data': [
            {'produto_id': 1, 'quantidade': 1}, 
            {'produto_id': 5, 'quantidade': 1}
        ]
    }),
    'status_pedido': 'Em Preparação',
    'status_pagamento': 'Efetuado',
    'pagamento_id': 'abc'
}

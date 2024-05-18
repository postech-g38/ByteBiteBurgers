from datetime import datetime
from bson import ObjectId


USUARIO_MODEL_CLIENTE_MOCK = {
    '_id': ObjectId('626bccb9697a12204fb22ea3'),
    'created_at': datetime.utcnow(),
    'updated_at': datetime.utcnow(),
    'deleted_at': None,
    'nome': 'Fulano De Tal',
    'senha': 'senha123',
    'cpf': '17132451081',
    'email': 'someone@email.com',
    'tipo': 'cliente'
}

USUARIO_MODEL_CLIENTE_DELETED_MOCK = {
    '_id': ObjectId('626bccb9697a12204fb22ea3'),
    'created_at': datetime.utcnow(),
    'updated_at': datetime.utcnow(),
    'deleted_at': datetime.utcnow(),
    'nome': 'Ciclano Daquilo',
    'senha': 'senha123',
    'cpf': '05049842093',
    'email': 'someone@email.com',
    'tipo': 'cliente'
}

USUARIO_MODEL_ADMIN_MOCK = {
    '_id': ObjectId('626bccb9697a12204fb22ea3'),
    'created_at': datetime.utcnow(),
    'updated_at': datetime.utcnow(),
    'deleted_at': None,
    'nome': 'Ciclano Daquilo',
    'senha': 'senha123',
    'cpf': '05049842093',
    'email': 'someone@email.com',
    'tipo': 'admin'
}

USUARIO_MODEL_ADMIN_DELETED_MOCK = {
    '_id': ObjectId('626bccb9697a12204fb22ea3'),
    'created_at': datetime.utcnow(),
    'updated_at': datetime.utcnow(),
    'deleted_at': datetime.utcnow(),
    'nome': 'Ciclano Daquilo',
    'senha': 'senha123',
    'cpf': '05049842093',
    'email': 'someone@email.com',
    'tipo': 'admin'
}

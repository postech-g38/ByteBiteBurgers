from enum import Enum


class UsuarioTipo(str, Enum):
    CLIENTE: str = 'cliente'
    ADMIN:   str = 'admin'

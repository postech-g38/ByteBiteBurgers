from typing import Any

from src.adapters.repositories import EntityRepository


class UsuarioService:
    def __init__(self, repository: EntityRepository) -> None:
        self.repository = repository
    
    def create_user(self, nome: str, senha: str, documento: str, tipo_id: str) -> dict[str,Any]:
        user = UserModel()
        self.repository.user.save(model=user)
        return {
            'data': 'key'
        }
    
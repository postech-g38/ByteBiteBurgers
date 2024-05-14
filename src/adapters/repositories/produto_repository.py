from sqlalchemy import select
from sqlalchemy.orm.session import Session
from fastapi import Depends

from src.adapters.repositories.sqlalchemy_repository import SQLAlchemyRepository
from src.adapters.database.models.produto_model import ProdutoModel
from src.adapters.database import get_database_session


class ProdutoRepository(SQLAlchemyRepository):
    def __init__(self, database_session: Session = Depends(get_database_session)) -> None:
        super().__init__(session=database_session)
        self.entity_model = ProdutoModel
      
    def get_by_categoria(self, categoria: str) -> list[ProdutoModel]:
        stmt = select(self.entity_model).where(self.entity_model.categoria == categoria)
        results = self.session_db.execute(stmt)
        return results.scalars().all()
    
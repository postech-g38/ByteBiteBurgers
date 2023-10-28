from src.adapters.repositories.sqlalchemy_repository import SQLAlchemyRepository
from src.adapters.database.models.checkout_model import CheckoutModel


class CheckoutRepository(SQLAlchemyRepository):
     def __init__(self, database_session) -> None:
        super().__init__(session=database_session)
        self.entity_model = CheckoutModel
        
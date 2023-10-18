from src.adapters.database.settings import sync_engine, get_session
from src.adapters.database.models.base_model import BaseModel

def create_database() -> None:
    """Create Database Tables from ORM, EDR will be created too"""
    BaseModel.metadata.create_all(bind=sync_engine)

def destroy_database() -> None:
    BaseModel.metadata.drop_all(bind=sync_engine)

def load_database(database_session, data: list) -> None:
    database_session.add_all(data)

from test.manual.models.usuario_model import USUARIO_MODEL_MOCK  # save dict on tests/manual/
from src.adapters.database.models.usuario_model import UsuarioModel

if __name__ == '__main__':
    create_database()
    with get_session as sess:
        load_database(
            database_session=sess,
            data=[
                # add models and data here
                UsuarioModel(**USUARIO_MODEL_MOCK),
            ]
        )
    
from src.adapters.database.settings import sync_engine
from src.adapters.database.models.base_model import BaseModel

def create_database() -> None:
    """Create Database Tables from ORM, EDR will be created too"""
    BaseModel.metadata.create_all(bind=sync_engine)

def destroy_database() -> None:
    BaseModel.metadata.drop_all(bind=sync_engine)

def load_database() -> None:
    pass


if __name__ == '__main__':
    create_database()
    
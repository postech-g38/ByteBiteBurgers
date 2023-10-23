from src.adapters.database.settings import sync_engine
from src.adapters.database.models.base_model import BaseModel

BaseModel.metadata.drop_all(bind=sync_engine, tables=tables, checkfirst=False)
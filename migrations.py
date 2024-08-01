from datetime import datetime
from json import dumps

from src.adapters.database.settings import sync_engine, get_session
from src.adapters.database.models.base_model import BaseModel
from src.adapters.database.models.pagamento_model import PagamentoModel


if __name__ == '__main__':
    # Para rodar o import de dados, devemos setar o ENVIRONMENT=dev e colocar as predenciais
    # do banco no .env.dev
    # rodar noterminalcomo python db.py
    BaseModel.metadata.create_all(sync_engine)

    # with get_session() as session:
    #     session.add_all(

    #     )

    # with get_session() as session:
    #     session.add_all(
            
    #     )

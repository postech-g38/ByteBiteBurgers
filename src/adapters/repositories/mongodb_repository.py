from typing import Dict, Any, List
from bson import ObjectId

from pymongo.client_session import ClientSession

from src.adapters.database.settings import client


class PyMongoRepository:
    def __init__(self, session: ClientSession, database: str, collection: str) -> None:
        self._session = session
        self._collection = client[database][collection]
    
    def get_all(self) -> List[Dict[str, Any]] | None:
        return self._collection.find(session=self._session)
    
    def search_by_id(self, model_id: ObjectId) -> Dict[str, Any] | None:
        return self._collection.find_one({'_id': model_id}, session=self._session)

    def save(self, data: Dict[str, Any]) -> ObjectId:
        return self._collection.insert_one(data, session=self._session).inserted_id
    
    def update(self, model_id: ObjectId, data: Dict[str, Any]) -> Dict[str, Any]:
        return self._collection.update_one({'_id': model_id}, {'$set': data}, upsert=False, session=self._session)

    def delete(self, model_id: ObjectId):
        return self._collection.delete_one({'_id': model_id}, session=self._session)

from typing import Any

from fastapi import APIRouter, Depends

from src.schemas.health_check_schema import HealthCheckResponse
from src.adapters.repositories import EntityRepository


router = APIRouter()


@router.get(
    path='/health_check', 
    response_model=HealthCheckResponse, 
    status_code=200,tags=['Health Check'], 
    description='Is API alive ?'
    )
def health_check(repository: EntityRepository = Depends()) -> dict[str, Any]:
    payload = {
        'status': 'alive',
        'message': 'hello world'
    }
    return HealthCheckResponse(payload)

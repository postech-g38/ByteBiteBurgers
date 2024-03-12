from typing import Any

from fastapi import APIRouter, Depends

from src.presenters.health_check_schema import HealthCheckResponse


router = APIRouter()


@router.get(
    path='/health_check', 
    response_model=HealthCheckResponse, 
    status_code=200,tags=['Health Check'], 
    description='Is API alive ?'
    )
def health_check() -> dict[str, Any]:
    # repository: EntityRepository = Depends()
    payload = {
        'status': 'alive',
        'message': 'hello world'
    }
    return HealthCheckResponse.model_validate(payload)

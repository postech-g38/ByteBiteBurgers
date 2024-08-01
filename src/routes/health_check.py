from typing import Any

from fastapi import APIRouter, Depends

from src.schemas.health_check_schema import HealthCheckResponse


router = APIRouter()


@router.get(
    path='/healthcheck', 
    response_model=HealthCheckResponse,
    tags=['Health Check'], 
    description='Is API alive ?'
)
def health_check():
    return HealthCheckResponse()

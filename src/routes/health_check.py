from typing import Any

from fastapi import APIRouter, Depends

from src.schemas.health_check_schema import HealthCheckResponse


router = APIRouter()


@router.route(
    path='/healthcheck', 
    methods=['GET', 'POST', 'HEAD'],
    status_code=200,
    response_model=HealthCheckResponse, 
    tags=['Health Check'], 
    description='Is API alive ?'
)
def health_check():
    return HealthCheckResponse()

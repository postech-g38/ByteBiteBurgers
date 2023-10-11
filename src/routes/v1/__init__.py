from fastapi import APIRouter

from src.routes.v1.usuario_route import router as user_router

router = APIRouter(prefix='/v1')

router.include_router(user_router)

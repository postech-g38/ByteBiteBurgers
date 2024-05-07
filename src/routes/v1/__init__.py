from fastapi import APIRouter

from src.routes.v1.usuario_route import router as usuario_router

router = APIRouter(prefix='/v1')
router.include_router(usuario_router)

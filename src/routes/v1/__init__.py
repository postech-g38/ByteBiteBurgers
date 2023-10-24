from fastapi import APIRouter

from src.routes.v1.usuario_route import router as user_router
from src.routes.v1.produto_route import router as produto_router

router = APIRouter(prefix='/v1')

router.include_router(user_router)
router.include_router(produto_router)

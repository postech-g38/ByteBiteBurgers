from fastapi import APIRouter

from src.routes.v1.pedido_route import router as pedido_route
from src.routes.v1.produto_route import router as produto_route

router = APIRouter(prefix='/v1')


router.include_router(pedido_route)
router.include_router(produto_route)

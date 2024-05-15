from fastapi import APIRouter

from src.routes.v1.pagamento_route import router as pagamento_router

router = APIRouter(prefix='/v1')

router.include_router(pagamento_router)

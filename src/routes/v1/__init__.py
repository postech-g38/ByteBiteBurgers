from fastapi import APIRouter

from .usuario_route import router as user_router

router = APIRouter('/v1')

router.include_router(user_router)

from fastapi import APIRouter
from backend.api.v1 import router as v1_router

from config.loader import load_config


config = load_config()

print(config.api_prefix.prefix)

router = APIRouter(
    prefix=config.api_prefix.prefix  # /api
)

router.include_router(v1_router)

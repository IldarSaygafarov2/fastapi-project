from .routes.categories import router as categories_router

from fastapi import APIRouter
from config.loader import load_config


config = load_config()

router = APIRouter(
    prefix=config.api_prefix.v1.prefix  # /v1
)

router.include_router(categories_router)


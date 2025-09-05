# http://127.0.0.1:8000/api/v1/categories/
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from config.loader import load_config
from pydantic import BaseModel
from backend.app.dependencies import get_repo
from infrastructure.database.repo.requests import RequestsRepo

config = load_config()
router = APIRouter(
    tags=['Categories'],
    prefix=config.api_prefix.v1.categories,  # api/v1/categories
)


class CategoryDTO(BaseModel):
    id: int
    name: str


class CategoryCreateDTO(BaseModel):
    name: str


@router.post('/')
async def create_category(
        data: CategoryCreateDTO,
        repo: Annotated[RequestsRepo, Depends(get_repo)]
) -> CategoryDTO:
    new_category = await repo.categories.add_category(name=data.name)
    return CategoryDTO.model_validate(new_category, from_attributes=True)


@router.get('/')  # обработка GET запроса
async def get_categories(
        repo: Annotated[RequestsRepo, Depends(get_repo)]
) -> list[CategoryDTO]:
    categories = await repo.categories.get_categories()
    return categories


# path parameters - параметры пути
# <str:username>
@router.get('/{category_id}', response_model=CategoryDTO)
async def get_category_by_id(
        category_id: int,
        repo: Annotated[RequestsRepo, Depends(get_repo)]
):
    category = await repo.categories.get_category_by_id(category_id=category_id)
    if category is None:
        raise HTTPException(status_code=404, detail=f'Category with {category_id=} not found')
    return CategoryDTO.model_validate(category, from_attributes=True)


@router.put('/{category_id}', response_model=CategoryDTO)
async def update_category(
        category_id: int,
        data: CategoryCreateDTO,
        repo: Annotated[RequestsRepo, Depends(get_repo)]
):
    updated_category = await repo.categories.update_category(category_id, data.name)
    if updated_category is None:
        raise HTTPException(status_code=404, detail=f'Category with {category_id=} not found')
    return CategoryDTO.model_validate(updated_category, from_attributes=True)
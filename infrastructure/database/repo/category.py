from .base import BaseRepo

import sqlalchemy as sa
from infrastructure.database.models.category import Category


class CategoryRepo(BaseRepo):
    async def add_category(self, name: str):
        query = sa.insert(Category).values(
            name=name
        ).returning(Category)  # INSERT INTO categories(name) VALUES (%s) RETURNING *
        result = await self.session.execute(query)
        await self.session.commit()  # отправка запроса в базу данных
        return result.scalar_one()

    async def get_categories(self):
        query = sa.select(Category)  # SELECT * FROM categories;
        result = await self.session.execute(query)
        return result.scalars().all()

    # ORM - object relation model
    # tortoise orm
    # sqlmodel
    async def get_category_by_id(self, category_id: int):  # SELECT * FROM categories WHERE id = %s;
        query = sa.select(Category).where(Category.id == category_id)  # None
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def delete_category(self):
        pass

    async def update_category(self, category_id: int, name: str):
        query = sa.update(Category).where(Category.id == category_id).values(name=name).returning(Category)  # UPDATE categories SET name = %s WHERE id = %s;
        result = await self.session.execute(query)
        await self.session.commit()
        return result.scalar_one_or_none()

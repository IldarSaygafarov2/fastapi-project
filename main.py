# fastapi-project

# main, master
# pull request

# exit()

# создать виртуальное окружение и сразу активировать
# python -m venv venv && venv\Scripts\activate


# pip install "fastapi[standard]"
# pip install fastapi
# pip freeze - показывает список библиотек и их версий

from fastapi import FastAPI
from pydantic import BaseModel

# объект АПИ запускающий проект
app = FastAPI(
    title='My API',
    description='My first API'
)


# класс аннотации типов данных для категорий
# data transfer object
class CategoryDTO(BaseModel):
    id: int
    name: str


# способы запуска проекта
# fastapi dev

# auth -> Авторизация, Регистрация, Выход с аккаунта
# cart -> Добавление в корзину, удаление с корзины, редактирование, оплата и оформление заказа


# http://127.0.0.1:8000/docs/


# аннотация типов данных
# схемы типов данных
@app.get('/api/categories/')  # обработка GET запроса
def get_categories() -> list[CategoryDTO]:
    categories = [CategoryDTO(id=i, name=f'category-{i}')
                  for i in range(1, 11)]
    return categories

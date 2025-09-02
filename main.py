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
from backend.api import router as api_router

# объект АПИ запускающий проект
app = FastAPI(
    title='My API',
    description='My first API'
)

app.include_router(api_router)


# класс аннотации типов данных для категорий
# data transfer object

# fastapi dev

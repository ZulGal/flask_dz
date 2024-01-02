# Напишите API для управления списком задач. Для этого создайте модель Task
# со следующими полями:
# ○ id: int (первичный ключ)
# ○ title: str (название задачи)
# ○ description: str (описание задачи)
# ○ done: bool (статус выполнения задачи)
# API должно поддерживать следующие операции:
# ○ Получение списка всех задач: GET /tasks/
# ○ Получение информации о конкретной задаче: GET /tasks/{task_id}/
# ○ Создание новой задачи: POST /tasks/
# ○ Обновление информации о задаче: PUT /tasks/{task_id}/
# ○ Удаление задачи: DELETE /tasks/{task_id}/
# 📌 Для валидации данных используйте параметры Field модели Task.
# 📌 Для работы с базой данных используйте SQLAlchemy и модуль databases

from contextlib import asynccontextmanager
from typing import List
from fastapi import FastAPI
from sqlalchemy import create_engine,select,insert,update,delete

import databases

from .pydantic_models import TaskIn, TaskOut
from .sqlalchemy_models import Base, Task

DATABASE_URL = 'sqlite:///task6_4.sqlite'
database = databases.Database(DATABASE_URL)
engine = create_engine(DATABASE_URL,connect_args={'check_same_thread': False})
Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app:FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

@app.get('/',response_model=List[TaskOut])
async def index():
    tasks = select(Task)

    return await database.fetch_all(tasks)

@app.post('/tasks/',response_model=TaskIn)
async def create_user(task:TaskIn):
    new_task = insert(Task).values(**task.model_dump())
    #     name = user.name,
    #     last_name = user.last_name,
    #     email = user.email,
    #     birthdate = user.birthdate,
    #     address = user.address
    # )
    await database.execute(new_task)
    return {**task.model_dump()}

@app.get('/tasks/{task_id}',response_model=TaskOut)
async def get_task(task_id:int):
    task = await database.fetch_one(select(Task).where(Task.id == task_id))
    return task

@app.put('/tasks/{task_id}',response_model=TaskOut)
async def update_task(task_id:int, new_task:TaskIn):
    task_update = update(Task).where(Task.id == task_id).values(**new_task.model_dump())
    await database.execute(task_update)
    return await database.fetch_one(select(Task).where (Task.id == task_id))

@app.delete('/tasks/{task_id}')
async def delete_task(task_id:int):
    task_delete = delete(Task).where(Task.id == task_id)
    await database.execute(task_delete)
    return{'result': 'success','deleted':task_id}
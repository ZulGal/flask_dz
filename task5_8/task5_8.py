# 📌 Необходимо создать API для управления списком задач. Каждая задача должна
# содержать заголовок и описание. Для каждой задачи должна быть возможность
# указать статус (выполнена/не выполнена).
# 📌 API должен содержать следующие конечные точки:
# ○ GET /tasks - возвращает список всех задач.
# ○ GET /tasks/{id} - возвращает задачу с указанным идентификатором.
# ○ POST /tasks - добавляет новую задачу.
# ○ PUT /tasks/{id} - обновляет задачу с указанным идентификатором.
# ○ DELETE /tasks/{id} - удаляет задачу с указанным идентификатором.
# 📌 Для каждой конечной точки необходимо проводить валидацию данных запроса и
# ответа. Для этого использовать библиотеку Pydantic.

from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from .pydantic_models import Task


app = FastAPI()
templates = Jinja2Templates(directory = 'flask_dz/task5_8/templates')
tasks = []

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        'tasks.html', {'request': request,'tasks': tasks})


@app.get('/tasks/{id}')
async def get_task(id: int):
    task = [task for task in tasks if task.id == id]
    return task

@app.post('/tasks/')
async def create_task(task: Task):
    tasks.append(task)
    return task

@app.put('/tasks/{task_id}')
async def update_task(task_id:int,new_task: Task):
    filtered_tasks = [task for task in tasks if task.id == task_id]
    if not filtered_tasks:
        return {'updated': False}
    task = filtered_tasks[0]

    task.name = new_task.title
    task.description = new_task.description
    task.status = new_task.status

    return{'updated': True, 'task': new_task}

@app.delete('/tasks/{task_id}/')
async def delete_task(task_id: int):
    filtered_tasks = [task for task in tasks if task.id == task_id]
    if not filtered_tasks:
        return {'deleted': False}
    task = filtered_tasks[0]
    tasks.remove(task)

    return {'deleted': True, 'task': task}

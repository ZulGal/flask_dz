from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Boolean, Column

Base = declarative_base()
# id: int (первичный ключ)
# ○ title: str (название задачи)
# ○ description: str (описание задачи)
# ○ done: bool (статус выполнения задачи)
class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer,primary_key=True)
    title = Column(String)
    description = Column(String)
    done = Column(Boolean)

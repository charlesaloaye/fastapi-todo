from database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime


class Todo(Base):

    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    is_complete = Column(Boolean)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

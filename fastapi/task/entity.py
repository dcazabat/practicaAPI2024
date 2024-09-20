# Declaracion del Modelo de Datos que se conecta con la BD
from sqlalchemy import ForeignKey
from default.defaultmodel import Base
from sqlalchemy import Column, Integer, String, Boolean, Date
from datetime import datetime

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(50), nullable=False)
    descripcion = Column(String(100), nullable=False)
    fecha = Column(Date, default= datetime.now())
    deleted = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

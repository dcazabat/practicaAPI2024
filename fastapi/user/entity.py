# Declaracion del Modelo de Datos que se conecta con la BD

from default.defaultmodel import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(100))
    password = Column(String(20), nullable=False)
    deleted = Column(Boolean, default=False)
    
    tasks = relationship('Task', backref='users', lazy=True)    
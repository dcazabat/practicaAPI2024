from sqlalchemy import ForeignKey
from default.defaultmodel import Base
from sqlalchemy import Column, Integer, String, Boolean, Date
from datetime import datetime

class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    autor = Column(String(50), nullable=False)
    publicado_en = Column(Date, default= datetime.now())
    isnb = Column(Integer, nullable=False)
    deleted = Column(Boolean, default=False)

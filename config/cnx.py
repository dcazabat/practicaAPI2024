from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from config import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

# Creamos las Session
sessionlocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)




from libros.config.cnx import SQLALCHEMY_DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Creacion del motor
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

# Creacion de sesion
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

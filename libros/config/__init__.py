import os
from dotenv import load_dotenv

load_dotenv()

STRCNX_local="sqlite:///basedb.db"

ENGINE=os.getenv('ENGINE')
HOST=os.getenv('HOST')
LIBROS=os.getenv('LIBROS')
PWDS=os.getenv('PWDS')
DBA=os.getenv('DBA')
PORT=os.getenv('PORT')

STRCNX_prod = f"{ENGINE}://{LIBROS}:{PWDS}@{HOST}:{PORT}/{DBA}"

if os.getenv('ENVIROMENT') == 'local':
    SQLALCHEMY_DATABASE_URI=STRCNX_local
else:
    SQLALCHEMY_DATABASE_URI=STRCNX_prod
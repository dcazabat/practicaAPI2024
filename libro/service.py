# Contiene todas las funciones que manejan la logica de Negocio (QUE ACCIONES REALIZO con la BD)
from libro.entity import User
from config.cnx import sessionlocal
from user.dto import CreateUser, DeleteUserDTO, UpdateUserDTO, UserDTO

# Devuelve todos los Usuarios Activos
def getUsers():
    try:
        db = sessionlocal()
        users = db.query(User).filter(User.deleted == False).all()
        if users:
            return users
        return None
    except Exception as e:
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Devuelve todos los Usuarios Inactivos
def getUsersInactive():
    try:
        db = sessionlocal()
        users = db.query(User).filter(User.deleted == True).all()
        if users:
            return users
        return None
    except Exception as e:
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Devuelve los datos del Usuario Inactivo o Activo
def getUser(id: int):
    try:
        db = sessionlocal()
        user = db.query(User).filter(User.id == id).first()
        if user:
            return user
        return None
    except Exception as e:
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Crea un Usuario dentro de la Base de Datos (POST)
def createUser(user: CreateUser):
    try:
        db = sessionlocal()
        user_new = User(
            name = user.name,
            firstname = user.firstname,
            lastname = user.lastname,
            email = user.email,
            password = user.password
        )
        db.add(user_new)
        db.commit()
        db.refresh(user_new)
        db.close()
        return user_new
    except Exception as e:
        db.rollback()
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Actualizacion de Datos del Usuario        
def updateUser(userupdate: UpdateUserDTO, id: int):
    try:
        db = sessionlocal()
        user_update = db.query(User).filter(User.id == int(id)).first()
        if user_update:
            user_update.firstname = userupdate.firstname
            user_update.lastname = userupdate.lastname
            user_update.email = userupdate.email
            db.commit()
            db.refresh(user_update)
            return user_update
        return None
    except Exception as e:
        db.rollback()
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Borrado LOGICO de Datos de Usuario 
def deleteUser(userdelete: DeleteUserDTO):
    try:
        db = sessionlocal()
        user_delete = db.query(User).filter(User.id == userdelete.id).first()
        if user_delete:
            user_delete.deleted = userdelete.deleted
            db.commit()
            db.refresh(user_delete)
            return user_delete
        return None
    except Exception as e:
        db.rollback()
        return f'Ocurrio un error, {e}'
    finally:
        db.close()
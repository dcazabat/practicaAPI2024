# Contiene todas las funciones que manejan la logica de Negocio (QUE ACCIONES REALIZO con la BD)
from task.entity import Task
from config.cnx import sessionlocal
from task.dto import CreateTask, DeleteTaskDTO, UpdateTaskDTO, TaskDTO

# Devuelve todos los Usuarios Activos
def getTasks():
    try:
        db = sessionlocal()
        tasks = db.query(Task).filter(Task.deleted == False).all()
        if tasks:
            return tasks
        return None
    except Exception as e:
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Devuelve todos los Usuarios Inactivos
def getTasksInactive():
    try:
        db = sessionlocal()
        tasks = db.query(Task).filter(Task.deleted == True).all()
        if tasks:
            return tasks
        return None
    except Exception as e:
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Devuelve los datos del Usuario Inactivo o Activo
def getTask(id: int):
    try:
        db = sessionlocal()
        task = db.query(Task).filter(Task.id == id).first()
        if task:
            return task
        return None
    except Exception as e:
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Crea un Usuario dentro de la Base de Datos (POST)
def createTask(task: CreateTask):
    try:
        db = sessionlocal()
        task_new = Task(
            titulo = task.titulo,
            descripcion = task.descripcion,
            user_id = task.user_id,
        )
        db.add(task_new)
        db.commit()
        db.refresh(task_new)
        db.close()
        return task_new
    except Exception as e:
        db.rollback()
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Actualizacion de Datos del Usuario        
def updateTask(taskupdate: UpdateTaskDTO):
    try:
        db = sessionlocal()
        task_update = db.query(Task).filter(Task.id == int(taskupdate.id)).first()
        if task_update:
            task_update.titulo = taskupdate.titulo
            task_update.descripcion = taskupdate.descripcion
            db.commit()
            db.refresh(task_update)
            return task_update
        return None
    except Exception as e:
        db.rollback()
        return f'Ocurrio un error, {e}'
    finally:
        db.close()

# Borrado LOGICO de Datos de Usuario 
def deleteTask(taskdelete: DeleteTaskDTO):
    try:
        db = sessionlocal()
        task_delete = db.query(Task).filter(Task.id == taskdelete.id).first()
        if task_delete:
            task_delete.deleted = taskdelete.deleted
            db.commit()
            db.refresh(task_delete)
            return task_delete
        return None
    except Exception as e:
        db.rollback()
        return f'Ocurrio un error, {e}'
    finally:
        db.close()
from task.entity import Task
from config.cnx import sessionlocal
from task.dto import CreateTask, TaskDTO, DeleteTaskDTO
from sqlalchemy.orm import joinedload

# Devuelve todas las Tareas con información del usuario
def getTasks():
    try:
        db = sessionlocal()
        tasks = db.query(Task).options(joinedload(Task.user)).all()
        if tasks:
            return tasks
        return None
    except Exception as e:
        return f'Ocurrió un error, {e}'
    finally:
        db.close()

# Devuelve los datos de una Tarea por su ID con información del usuario
def getTask(id: int):
    try:
        db = sessionlocal()
        task = db.query(Task).options(joinedload(Task.user)).filter(Task.id == id).first()
        if task:
            return task
        return None
    except Exception as e:
        return f'Ocurrió un error, {e}'
    finally:
        db.close()

# Crea una Tarea dentro de la Base de Datos (POST)
def createTask(task: CreateTask, user_id: int):
    try:
        db = sessionlocal()
        task_new = Task(
            titulo = task.titulo,
            descripcion = task.descripcion,
            user_id = user_id
        )
        db.add(task_new)
        db.commit()
        db.refresh(task_new)
        return task_new
    except Exception as e:
        db.rollback()
        return f'Ocurrió un error, {e}'
    finally:
        db.close()

# Actualización de Datos de la Tarea        
def updateTask(taskupdate: TaskDTO):
    try:
        db = sessionlocal()
        task_to_update = db.query(Task).filter(Task.id == taskupdate.id).first()
        if task_to_update:
            task_to_update.titulo = taskupdate.titulo
            task_to_update.descripcion = taskupdate.descripcion
            task_to_update.completado = taskupdate.completado
            db.commit()
            db.refresh(task_to_update)
            return task_to_update
        return None
    except Exception as e:
        db.rollback()
        return f'Ocurrió un error, {e}'
    finally:
        db.close()

# Borrado lógico de una Tarea
def deleteTask(taskdelete: DeleteTaskDTO):
    try:
        db = sessionlocal()
        task_to_delete = db.query(Task).filter(Task.id == taskdelete.id).first()
        if task_to_delete:
            task_to_delete.deleted = taskdelete.deleted
            db.commit()
            db.refresh(task_to_delete)
            return task_to_delete
        return None
    except Exception as e:
        db.rollback()
        return f'Ocurrió un error, {e}'
    finally:
        db.close()

from sqlalchemy.orm import Session
from openapi_server.models.modelsORM import Usuario, Perfil

# Crear un usuario
def crear_usuario(db: Session, nombre: str, apellido: str, email: str, contrasena: str, fecha_nacimiento=None):
    nuevo_usuario = Usuario(
        nombre=nombre,
        apellido=apellido,
        email=email,
        contrasena=contrasena,
        fecha_nacimiento=fecha_nacimiento
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def login_usuario(db: Session, email: str, contrasena: str):
    if db.query(Usuario).filter(Usuario.email == email, Usuario.contrasena == contrasena).first():
        print("Usuario logueado")
        return True
    else:
        print("Usuario no logueado")
        return False

def obtener_id_usuario(db: Session, email: str) -> int:
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    return usuario.id

# Actualizar un usuario
def actualizar_usuario(db: Session, usuario_id: int, nombre: str = None, apellido: str = None, email: str = None, contrasena: str = None):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario:
        if nombre:
            usuario.nombre = nombre
        if apellido:
            usuario.apellido = apellido
        if email:
            usuario.email = email
        if contrasena:
            usuario.contrasena = contrasena
        db.commit()
        return True
    return False

# Eliminar un usuario
def eliminar_usuario(db: Session, usuario_id: int) -> bool:
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario:
        db.delete(usuario)
        db.commit()
        return True
    return False
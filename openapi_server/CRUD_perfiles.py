from sqlalchemy.orm import Session
from openapi_server.models.modelsORM import Usuario, Perfil

def obtener_id_perfil(db: Session, id_usuario: int) -> int:
    perfil = db.query(Perfil).filter(Perfil.usuario_id == id_usuario).first()
    return perfil.id

def obtener_perfil_usuario(db: Session, id_usuario: int) -> bool:
    perfil = db.query(Perfil).filter(Perfil.usuario_id == id_usuario).first()
    return perfil is not None
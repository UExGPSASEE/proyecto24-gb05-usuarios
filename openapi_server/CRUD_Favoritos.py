from sqlalchemy.orm import Session
from openapi_server.models.modelsORM import Usuario, Perfil, Favoritos

def obtener_favoritos_usuario(db: Session, id_usuario: int, id_perfil: int) -> Favoritos:
    return db.query(Favoritos).filter(Favoritos.idusuario == id_usuario and Favoritos.idperfil == id_perfil).all()

def añadir_favorito_usuario(db: Session, id_usuario: int,id_perfil: int ,id_contenido: int) -> None:
    favorito = Favoritos(idusuario=id_usuario,idperfil= id_perfil,idpelicula=id_contenido)
    db.add(favorito)
    db.commit()


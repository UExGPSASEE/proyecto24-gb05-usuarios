from sqlalchemy.orm import Session
from openapi_server.models.modelsORM import Usuario, Perfil, MetodoPago

def obtener_id_tarjeta(db: Session, id_usuario: int) -> int:
    tarjeta = db.query(MetodoPago).filter(MetodoPago.usuario_id == id_usuario).first()
    return tarjeta.id

def agregar_metodo_pago(db: Session, id_usuario: int, tipo: str, numero: str, fecha_expiracion: str, cvv: str) -> None:
    tarjeta = MetodoPago(usuario_id=id_usuario, tipo_tarjeta=tipo, numero_tarjeta=numero, fecha_expiracion=fecha_expiracion, cvv=cvv)
    db.add(tarjeta)
    db.commit()

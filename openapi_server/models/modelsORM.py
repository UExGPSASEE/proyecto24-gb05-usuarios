from sqlalchemy import Column, Integer, String, Date, TIMESTAMP, LargeBinary
from sqlalchemy.sql import func
# openapi_server/models/modelsORM.py
from openapi_server.database import Base


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    contrasena = Column(String(255), nullable=False)
    avatar = Column(LargeBinary, nullable=True)
    fecha_nacimiento = Column(Date, nullable=True)
    fecha_creacion = Column(TIMESTAMP, server_default=func.now())

class Perfil(Base):
    __tablename__ = 'perfiles'

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, nullable=False)
    nombre_perfil = Column(String(50), nullable=False)
    avatar_perfil = Column(LargeBinary, nullable=True)

class MetodoPago(Base):
    __tablename__ = 'metodos_pago'

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, nullable=False)
    tipo_tarjeta = Column(String(50), nullable=False)
    numero_tarjeta = Column(String(50), nullable=False)
    fecha_expiracion = Column(Date, nullable=False)
    cvv = Column(String(3), nullable=False)

class Favoritos(Base):
    __tablename__ = 'favoritos'

    id = Column(Integer, primary_key=True, index=True)
    idusuario = Column(Integer, nullable=False)
    idperfil = Column(Integer, nullable=False)
    idpelicula = Column(Integer, nullable=False)

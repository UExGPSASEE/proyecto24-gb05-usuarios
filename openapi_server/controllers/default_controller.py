import connexion

from openapi_server.models.login import Login
from openapi_server.models.metodo_pago import MetodoPago as MetodoPagoModel
from openapi_server.models.perfil_usuario import PerfilUsuario
from openapi_server.models.usuario import Usuario as UsuarioModel
from openapi_server.models.Favoritos import Favoritos
from openapi_server.models.modelsORM import (
    Usuario as UsuarioORM,
    Perfil as PerfilORM,
    MetodoPago as MetodoPagoORM,
    Favoritos as FavoritosORM
)
from openapi_server import CRUD_usuarios, CRUD_perfiles, CRUD_metodosPago, CRUD_Favoritos 
from openapi_server.database import SessionLocal
from flask import Response
from sqlalchemy.exc import IntegrityError
from flask import jsonify
def agregar_metodo_pago():
    """Añadir método de pago al usuario autenticado."""
    db = SessionLocal()
    try:
        if not connexion.request.is_json:
            return 'El contenido de la solicitud no es JSON', 400

        metodo_pago_data = connexion.request.get_json()
        CRUD_metodosPago.agregar_metodo_pago(
            db,
            usuario_logeado,
            metodo_pago_data['tipoTarjeta'],
            metodo_pago_data['numeroTarjeta'],
            metodo_pago_data['fechaExpiracion'],
            metodo_pago_data['cvv']
        )
        return 'Método de pago añadido correctamente', 201
    except Exception as e:
        print(f"Error al añadir el método de pago: {e}")
        db.rollback()
        return 'Error al añadir el método de pago', 500
    finally:
        db.close()

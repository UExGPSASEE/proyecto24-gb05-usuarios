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

# Variables globales para mantener el estado del usuario y el perfil actual
usuario_logeado = None
perfil_actual = None


from flask import Response
def login_usuario():
    """Autenticación de usuario."""
    db = SessionLocal()
    global usuario_logeado, perfil_actual
    try:
        if not connexion.request.is_json:
            return Response('El contenido de la solicitud no es JSON', status=400, content_type='text/plain; charset=utf-8')

        login_data = connexion.request.get_json()
        correo_electronico = login_data.get('correoElectronico')
        contrasena = login_data.get('contrasena')

        if CRUD_usuarios.login_usuario(db, correo_electronico, contrasena):
            usuario_logeado = CRUD_usuarios.obtener_id_usuario(db, correo_electronico)

            if CRUD_perfiles.obtener_perfil_usuario(db, usuario_logeado):
                perfil_actual = CRUD_perfiles.obtener_id_perfil(db, usuario_logeado)
                return Response('Usuario autenticado correctamente', status=200, content_type='text/plain; charset=utf-8')
            else:
                return Response('Usuario autenticado correctamente, pero no tiene perfiles', status=200, content_type='text/plain; charset=utf-8')
        else:
            return Response('Credenciales incorrectas', status=401, content_type='text/plain; charset=utf-8')
    except Exception as e:
        print(f"Error al autenticar el usuario: {e}")
        return Response('Error al autenticar el usuario', status=500, content_type='text/plain; charset=utf-8')
    finally:
        db.close()

def registrar_usuario():
    """Registro de nuevo usuario."""
    if not connexion.request.is_json:
        return Response('El contenido de la solicitud no es JSON', status=400, content_type='text/plain; charset=utf-8')

    usuario_data = connexion.request.get_json()

    # Validación de campos requeridos
    required_fields = ['nombreUsuario', 'apellido', 'correoElectronico', 'contrasena', 'fechaNacimiento']
    if not all(field in usuario_data for field in required_fields):
        return Response('Faltan campos requeridos', status=400, content_type='text/plain; charset=utf-8')

    db = SessionLocal()
    try:
        CRUD_usuarios.crear_usuario(
            db,
            usuario_data['nombreUsuario'],
            usuario_data['apellido'],
            usuario_data['correoElectronico'],
            usuario_data['contrasena'],
            usuario_data['fechaNacimiento']
        )
        return Response('Usuario registrado correctamente', status=201, content_type='text/plain; charset=utf-8')
    except IntegrityError:
        db.rollback()
        return Response('El usuario ya está registrado', status=409, content_type='text/plain; charset=utf-8')
    except Exception as e:
        print(f"Error al registrar el usuario: {e}")
        db.rollback()
        return Response('Error al registrar el usuario', status=500, content_type='text/plain; charset=utf-8')
    finally:
        db.close()

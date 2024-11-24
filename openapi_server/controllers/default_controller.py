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

def modificar_usuario():
    """Modificación de datos del usuario principal."""
    db = SessionLocal()
    try:
        if usuario_logeado is None:
            return Response('Usuario no autenticado', status=401, content_type='text/plain; charset=utf-8')

        if not connexion.request.is_json:
            return Response('El contenido de la solicitud no es JSON', status=400, content_type='text/plain; charset=utf-8')

        usuario_data = connexion.request.get_json()

        # Validación de campos requeridos
        if not any(key in usuario_data for key in ['nombreUsuario', 'apellido', 'correoElectronico', 'contrasena']):
            return Response('Faltan datos para actualizar el usuario', status=400, content_type='text/plain; charset=utf-8')

        actualizado = CRUD_usuarios.actualizar_usuario(
            db,
            usuario_logeado,
            usuario_data.get('nombreUsuario'),
            usuario_data.get('apellido'),
            usuario_data.get('correoElectronico'),
            usuario_data.get('contrasena')
        )

        if actualizado:
            return Response('Usuario modificado correctamente', status=200, content_type='text/plain; charset=utf-8')
        else:
            return Response('Usuario no encontrado', status=404, content_type='text/plain; charset=utf-8')
    except Exception as e:
        print(f"Error al modificar el usuario: {e}")
        return Response('Error al modificar el usuario', status=500, content_type='text/plain; charset=utf-8')
    finally:
        db.close()

def eliminar_usuario():
    """Eliminar el usuario autenticado."""
    db = SessionLocal()
    global usuario_logeado
    try:
        # Validar si el usuario está autenticado
        if usuario_logeado is None:
            return Response('Usuario no autenticado', status=401, content_type='text/plain; charset=utf-8')

        # Intentar eliminar al usuario
        eliminado = CRUD_usuarios.eliminar_usuario(db, usuario_logeado)

        if eliminado:
            usuario_logeado = None  # Reiniciar la sesión global
            return Response('Usuario eliminado correctamente', status=200, content_type='text/plain; charset=utf-8')
        else:
            return Response('Usuario no encontrado', status=404, content_type='text/plain; charset=utf-8')

    except Exception as e:
        print(f"Error al eliminar el usuario: {e}")
        return Response('Error al eliminar el usuario', status=500, content_type='text/plain; charset=utf-8')
    finally:
        db.close()

def crear_perfil():
    """Crear un nuevo perfil de usuario (multicuentas)."""
    db = SessionLocal()
    global perfil_actual
    try:
        # Verificar si el contenido de la solicitud es JSON
        if not connexion.request.is_json:
            return Response('El contenido de la solicitud no es JSON', status=400,
                            content_type='text/plain; charset=utf-8')

        # Obtener datos del perfil desde la solicitud
        perfil_data = connexion.request.get_json()
        nombre_perfil = perfil_data.get('nombrePerfil')

        # Validar que el nombre del perfil está presente
        if not nombre_perfil:
            return Response('El nombre del perfil es obligatorio', status=400,
                            content_type='text/plain; charset=utf-8')

        # Crear el perfil en la base de datos
        CRUD_perfiles.agregar_perfil_usuario(db, usuario_logeado, nombre_perfil)

        # Si no hay un perfil actual, configurarlo como el creado
        if perfil_actual is None:
            perfil_actual = CRUD_perfiles.obtener_id_perfil_por_nombre(
                db, usuario_logeado, nombre_perfil
            )

        # Respuesta exitosa
        return Response('Perfil creado correctamente', status=201, content_type='text/plain; charset=utf-8')

    except IntegrityError:
        db.rollback()
        return Response('El perfil ya existe', status=409, content_type='text/plain; charset=utf-8')
    except Exception as e:
        print(f"Error al crear el perfil: {e}")
        db.rollback()
        return Response('Error al crear el perfil', status=500, content_type='text/plain; charset=utf-8')
    finally:
        db.close()

from flask import Response

def añadir_favorito():
    """Añadir contenido a favoritos."""
    db = SessionLocal()
    try:
        if not connexion.request.is_json:
            return Response('El contenido de la solicitud no es JSON', status=400, content_type='text/plain; charset=utf-8')

        favorito_data = connexion.request.get_json()

        # Verificar si hay un perfil seleccionado
        if perfil_actual is None:
            return Response('Perfil no seleccionado, no se puede agregar el contenido', status=400, content_type='text/plain; charset=utf-8')

        # Verificar si falta el ID del contenido
        if 'peliculaId' not in favorito_data:
            return Response('El ID del contenido es requerido', status=400, content_type='text/plain; charset=utf-8')

        # Añadir favorito si todo está correcto
        CRUD_Favoritos.añadir_favorito_usuario(db, usuario_logeado, perfil_actual, favorito_data['peliculaId'])
        return Response('Contenido añadido a favoritos correctamente', status=201, content_type='text/plain; charset=utf-8')

    except Exception as e:
        print(f"Error al añadir el contenido a favoritos: {e}")
        db.rollback()
        return Response('Error al añadir el contenido a favoritos', status=500, content_type='text/plain; charset=utf-8')

    finally:
        db.close()
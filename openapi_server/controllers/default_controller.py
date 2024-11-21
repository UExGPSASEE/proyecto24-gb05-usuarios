import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.login import Login  # noqa: E501
from openapi_server.models.metodo_pago import MetodoPago  # noqa: E501
from openapi_server.models.perfil_usuario import PerfilUsuario  # noqa: E501
from openapi_server.models.usuario import Usuario  # noqa: E501
from openapi_server.models.usuario_registro import UsuarioRegistro  # noqa: E501
from openapi_server import util


def agregar_metodo_pago(id, metodo_pago):  # noqa: E501
    """Añadir método de pago

    Permite añadir un nuevo método de pago a la cuenta del usuario. # noqa: E501

    :param id: ID del usuario
    :type id: int
    :param metodo_pago: 
    :type metodo_pago: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        metodo_pago = MetodoPago.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def cambiar_perfil(id, perfil_usuario):  # noqa: E501
    """Cambiar de perfil

    Cambia entre perfiles de usuario disponibles bajo la cuenta principal. # noqa: E501

    :param id: ID del usuario
    :type id: int
    :param perfil_usuario: 
    :type perfil_usuario: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        perfil_usuario = PerfilUsuario.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def crear_perfil(id, perfil_usuario):  # noqa: E501
    """Crear un nuevo perfil de usuario (multicuentas)

    Permite al usuario principal crear múltiples perfiles bajo la misma cuenta para diferentes personas. # noqa: E501

    :param id: ID del usuario
    :type id: int
    :param perfil_usuario: 
    :type perfil_usuario: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        perfil_usuario = PerfilUsuario.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def eliminar_perfil(id):  # noqa: E501
    """Eliminar perfil

    Elimina uno de los perfiles asociados a la cuenta principal del usuario. # noqa: E501

    :param id: ID del usuario
    :type id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def eliminar_usuario():  # noqa: E501
    """Eliminar usuario principal

    Elimina la cuenta del usuario principal y todos sus perfiles asociados. # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def login_usuario(login):  # noqa: E501
    """Autenticación de usuario

    Autentica a un usuario usando su correo electrónico y contraseña. # noqa: E501

    :param login: 
    :type login: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        login = Login.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def modificar_usuario(usuario):  # noqa: E501
    """Modificación de datos del usuario principal

    Modifica los datos personales del usuario principal, como correo electrónico, avatar o contraseña. # noqa: E501

    :param usuario: 
    :type usuario: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        usuario = Usuario.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def registrar_usuario(usuario_registro):  # noqa: E501
    """Registro de nuevo usuario

    Permite registrar un nuevo usuario principal en la plataforma Cineverse. Este usuario puede crear perfiles adicionales (multicuentas) y gestionar métodos de pago. # noqa: E501

    :param usuario_registro: 
    :type usuario_registro: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        usuario_registro = UsuarioRegistro.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def usuarios_id_get(id):  # noqa: E501
    """Obtener datos del usuario principal

    Obtiene la información del usuario principal, incluyendo su lista de perfiles de multicuentas. # noqa: E501

    :param id: ID del usuario
    :type id: int

    :rtype: Union[Usuario, Tuple[Usuario, int], Tuple[Usuario, int, Dict[str, str]]
    """
    return 'do some magic!'

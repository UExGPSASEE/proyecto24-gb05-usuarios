from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class PerfilUsuario(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, nombre_perfil=None, avatar_perfil=None):  # noqa: E501
        """PerfilUsuario - a model defined in OpenAPI

        :param id: The id of this PerfilUsuario.  # noqa: E501
        :type id: int
        :param nombre_perfil: The nombre_perfil of this PerfilUsuario.  # noqa: E501
        :type nombre_perfil: str
        :param avatar_perfil: The avatar_perfil of this PerfilUsuario.  # noqa: E501
        :type avatar_perfil: str
        """
        self.openapi_types = {
            'id': int,
            'nombre_perfil': str,
            'avatar_perfil': str
        }

        self.attribute_map = {
            'id': 'id',
            'nombre_perfil': 'nombrePerfil',
            'avatar_perfil': 'avatarPerfil'
        }

        self._id = id
        self._nombre_perfil = nombre_perfil
        self._avatar_perfil = avatar_perfil

    @classmethod
    def from_dict(cls, dikt) -> 'PerfilUsuario':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PerfilUsuario of this PerfilUsuario.  # noqa: E501
        :rtype: PerfilUsuario
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this PerfilUsuario.


        :return: The id of this PerfilUsuario.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this PerfilUsuario.


        :param id: The id of this PerfilUsuario.
        :type id: int
        """

        self._id = id

    @property
    def nombre_perfil(self) -> str:
        """Gets the nombre_perfil of this PerfilUsuario.


        :return: The nombre_perfil of this PerfilUsuario.
        :rtype: str
        """
        return self._nombre_perfil

    @nombre_perfil.setter
    def nombre_perfil(self, nombre_perfil: str):
        """Sets the nombre_perfil of this PerfilUsuario.


        :param nombre_perfil: The nombre_perfil of this PerfilUsuario.
        :type nombre_perfil: str
        """

        self._nombre_perfil = nombre_perfil

    @property
    def avatar_perfil(self) -> str:
        """Gets the avatar_perfil of this PerfilUsuario.


        :return: The avatar_perfil of this PerfilUsuario.
        :rtype: str
        """
        return self._avatar_perfil

    @avatar_perfil.setter
    def avatar_perfil(self, avatar_perfil: str):
        """Sets the avatar_perfil of this PerfilUsuario.


        :param avatar_perfil: The avatar_perfil of this PerfilUsuario.
        :type avatar_perfil: str
        """

        self._avatar_perfil = avatar_perfil

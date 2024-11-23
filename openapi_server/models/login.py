from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class Login(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, correo_electronico=None, contrasena=None):  # noqa: E501
        """Login - a model defined in OpenAPI

        :param correo_electronico: The correo_electronico of this Login.  # noqa: E501
        :type correo_electronico: str
        :param contrasea: The contrasea of this Login.  # noqa: E501
        :type contrasea: str
        """
        self.openapi_types = {
            'correo_electronico': str,
            'contrasena': str
        }

        self.attribute_map = {
            'correo_electronico': 'correoElectronico',
            'contrasena': 'contrasena'
        }

        self._correo_electronico = correo_electronico
        self._contrasena = contrasena

    @classmethod
    def from_dict(cls, dikt) -> 'Login':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Login of this Login.  # noqa: E501
        :rtype: Login
        """
        return util.deserialize_model(dikt, cls)

    @property
    def correo_electronico(self) -> str:
        """Gets the correo_electronico of this Login.


        :return: The correo_electronico of this Login.
        :rtype: str
        """
        return self._correo_electronico

    @correo_electronico.setter
    def correo_electronico(self, correo_electronico: str):
        """Sets the correo_electronico of this Login.


        :param correo_electronico: The correo_electronico of this Login.
        :type correo_electronico: str
        """

        self._correo_electronico = correo_electronico

    @property
    def contrasena(self) -> str:
        """Gets the contrasea of this Login.


        :return: The contrasea of this Login.
        :rtype: str
        """
        return self.contrasena

    @contrasena.setter
    def contrasena(self, contrasena: str):
        """Sets the contrasea of this Login.


        :param contrasea: The contrasea of this Login.
        :type contrasea: str
        """

        self.contrasena = contrasena

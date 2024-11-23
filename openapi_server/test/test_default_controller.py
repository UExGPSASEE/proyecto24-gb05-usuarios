import unittest

from flask import json

from openapi_server.models.login import Login  # noqa: E501
from openapi_server.models.metodo_pago import MetodoPago  # noqa: E501
from openapi_server.models.perfil_usuario import PerfilUsuario  # noqa: E501
from openapi_server.models.usuario import Usuario  # noqa: E501
from openapi_server.models.usuario_registro import UsuarioRegistro  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_agregar_metodo_pago(self):
        """Test case for agregar_metodo_pago

        Añadir método de pago
        """
        metodo_pago = {"cvv":"cvv","tipoTarjeta":"Visa","fechaExpiracion":"2000-01-23","id":0,"numeroTarjeta":"numeroTarjeta"}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/usuarios/{id}/metodos-pago'.format(id=56),
            method='POST',
            headers=headers,
            data=json.dumps(metodo_pago),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cambiar_perfil(self):
        """Test case for cambiar_perfil

        Cambiar de perfil
        """
        perfil_usuario = {"avatarPerfil":"avatarPerfil","id":6,"nombrePerfil":"nombrePerfil"}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/usuarios/{id}/perfiles'.format(id=56),
            method='PUT',
            headers=headers,
            data=json.dumps(perfil_usuario),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_crear_perfil(self):
        """Test case for crear_perfil

        Crear un nuevo perfil de usuario (multicuentas)
        """
        perfil_usuario = {"avatarPerfil":"avatarPerfil","id":6,"nombrePerfil":"nombrePerfil"}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/usuarios/{id}/perfiles'.format(id=56),
            method='POST',
            headers=headers,
            data=json.dumps(perfil_usuario),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_eliminar_perfil(self):
        """Test case for eliminar_perfil

        Eliminar perfil
        """
        headers = { 
        }
        response = self.client.open(
            '/api/usuarios/{id}/perfiles'.format(id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_eliminar_usuario(self):
        """Test case for eliminar_usuario

        Eliminar usuario principal
        """
        headers = { 
        }
        response = self.client.open(
            '/api/usuarios',
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_login_usuario(self):
        """Test case for login_usuario

        Autenticación de usuario
        """
        login = {"correoElectronico":"correoElectronico","contraseña":"contraseña"}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/usuarios/login',
            method='POST',
            headers=headers,
            data=json.dumps(login),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modificar_usuario(self):
        """Test case for modificar_usuario

        Modificación de datos del usuario principal
        """
        usuario = {"perfiles":[{"avatarPerfil":"avatarPerfil","id":6,"nombrePerfil":"nombrePerfil"},{"avatarPerfil":"avatarPerfil","id":6,"nombrePerfil":"nombrePerfil"}],"id":0,"nombreUsuario":"nombreUsuario","avatar":"avatar","correoElectronico":"correoElectronico"}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/usuarios',
            method='PUT',
            headers=headers,
            data=json.dumps(usuario),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_registrar_usuario(self):
        """Test case for registrar_usuario

        Registro de nuevo usuario
        """
        usuario_registro = {"nombreUsuario":"nombreUsuario","correoElectronico":"correoElectronico","contraseña":"contraseña"}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/usuarios',
            method='POST',
            headers=headers,
            data=json.dumps(usuario_registro),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuarios_id_get(self):
        """Test case for usuarios_id_get

        Obtener datos del usuario principal
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/usuarios/{id}'.format(id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

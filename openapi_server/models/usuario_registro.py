from openapi_server.models.base_model import Model

class UsuarioRegistro(Model):
    # Inicialización
    def __init__(self, nombre_usuario=None, apellido=None, correo_electronico=None, contrasena=None, fecha_nacimiento=None):
        self.openapi_types = {
            'nombre_usuario': str,
            'apellido': str,
            'correo_electronico': str,
            'contrasena': str,  # Aquí asegurarse que sea 'contrasena'
            'fecha_nacimiento': str
        }
        self.attribute_map = {
            'nombre_usuario': 'nombreUsuario',
            'apellido': 'apellido',
            'correo_electronico': 'correoElectronico',
            'contrasena': 'contrasena',  # Aquí asegurarse que sea 'contrasena'
            'fecha_nacimiento': 'fechaNacimiento'
        }

        self._nombre_usuario = nombre_usuario
        self._apellido = apellido
        self._correo_electronico = correo_electronico
        self._contrasena = contrasena  # Aquí asegurarse que sea '_contrasena'
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def contrasena(self) -> str:
        """Gets the contrasena of this UsuarioRegistro."""
        return self._contrasena

    @contrasena.setter
    def contrasena(self, contrasena: str):
        """Sets the contrasena of this UsuarioRegistro."""
        self._contrasena = contrasena

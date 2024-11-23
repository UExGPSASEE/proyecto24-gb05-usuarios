from openapi_server import util
from openapi_server.models.base_model import Model

class Favoritos(Model):
    def __init__(self, id=None, id_usuario=None, id_contenido=None):
        self.openapi_types = {
            'id': int,
            'id_usuario': int,
            'id_contenido': int
        }

        self.attribute_map = {
            'id': 'id',
            'id_usuario': 'idUsuario',
            'id_contenido': 'idcontenido'
        }

        self._id = id
        self._id_usuario = id_usuario
        self._id_contenido = id_contenido

    @classmethod
    def from_dict(cls, dikt) -> 'Favoritos':
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def id_usuario(self) -> int:
        return self._id_usuario
    
    @property
    def id_contenido(self) -> int:
        return self._id_contenido
    
    @id.setter
    def id(self, id: int):
        self._id = id
    
    @id_usuario.setter
    def id_usuario(self, id_usuario: int):
        self._id_usuario = id_usuario
    
    @id_contenido.setter
    def id_contenido(self, id_contenido: int):
        self._id_contenido = id_contenido

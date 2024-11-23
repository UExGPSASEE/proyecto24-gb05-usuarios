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


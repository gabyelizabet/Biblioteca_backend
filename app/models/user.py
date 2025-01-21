from .database import add_bibliotecarios, add_lector, get_usuario_by_usuario, verify_password

class User:
    @staticmethod
    def add_bibliotecario(data):
        return add_bibliotecarios(data['nombre'], data['apellido'], data['email'], data['telefono'], 
                                  data['usuario'], data['contrasena'])

    @staticmethod
    def add_lector(data):
        return add_lector(data['nombre'], data['apellido'], data['email'], data['telefono'], 
                          data['matricula'], data['usuario'], data['contrasena'])

    @staticmethod
    def verify_login(usuario, contrasena):
        usuario_obj = get_usuario_by_usuario(usuario)
        if usuario_obj and verify_password(usuario_obj['contrasena'], contrasena):
            return usuario_obj
        return None

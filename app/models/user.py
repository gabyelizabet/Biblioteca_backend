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
        # Verifica si el usuario no existe
        if not usuario_obj:
            raise ValueError('Usuario no encontrado')

        # Verifica si la contraseña es incorrecta
        if not verify_password(usuario_obj['contrasena'], contrasena):
            raise ValueError('Contraseña incorrecta')

        return usuario_obj  # Si el usuario y la contraseña son correctos, retorna el usuario
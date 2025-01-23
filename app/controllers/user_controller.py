from flask import jsonify, request, session
from ..models.user import User

class UserController:
    @staticmethod
    def register_bibliotecario(data):
        User.add_bibliotecario(data)
        return jsonify({'message': 'Bibliotecario registered successfully'}), 201

    @staticmethod
    def register_lector(data):
        User.add_lector(data)
        return jsonify({'message': 'Lector registered successfully'}), 201

    @staticmethod
    def login():
        try:
            data = request.json
            user = User.verify_login(data['usuario'], data['contrasena'])  # Verifica las credenciales

            # Si el usuario es válido, establecer sesión y retornar respuesta exitosa
            session['usuario'] = user['usuario']
            session['tipo_usuario'] = 'lector' if 'matricula' in user else 'bibliotecario'
            return jsonify({'message': 'Login successful'}), 200

        except ValueError as e:
            # Usuario no encontrado o contraseña incorrecta
            return jsonify({'message': str(e)}), 401  # Devuelve el mensaje de error
        except Exception as e:
            # Manejo de otras excepciones
            return jsonify({'message': 'Error inesperado'}), 500

    """@staticmethod
    def login():
        data = request.json
        user = User.verify_login(data['usuario'], data['contrasena'])
        if user:
            session['usuario'] = user['usuario']
            if 'matricula' in user:  # Si el usuario tiene matrícula, es un lector
                session['tipo_usuario'] = 'lector'
            else:  # Si no tiene matrícula, es un bibliotecario
                session['tipo_usuario'] = 'bibliotecario'
            
            return jsonify({'message': 'Login successful'}), 200
        return jsonify({'message': 'Invalid credentials'}), 401"""


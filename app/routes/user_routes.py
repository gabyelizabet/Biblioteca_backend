from flask import Blueprint, jsonify, request, session
from app.controllers.user_controller import UserController

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/api/lectores', methods=['POST'])
def register_lector():
    data = request.json
    UserController.register_lector(data)
    return jsonify({'message': 'Lector registrado exitosamente!'}), 201

@user_routes.route('/api/bibliotecarios', methods=['POST'])
def register_bibliotecario():
    data = request.json
    UserController.register_bibliotecario(data)
    return jsonify({'message': 'Bibliotecario registrado exitosamente!'}), 201

@user_routes.route('/api/login', methods=['POST'])
def login_usuario():
    data = request.json
    user = UserController.login(data['usuario'], data['contrasena'])
    if user:
        session['usuario'] = user['usuario']
        session['tipo_usuario'] = 'lector' if 'matricula' in user else 'bibliotecario'
        return jsonify({'message': 'Sesión iniciada exitosamente'}), 200
    return jsonify({'message': 'Usuario o contraseña incorrectos'}), 401

@user_routes.route('/api/logout', methods=['POST'])
def logout_usuario():
    session.pop('usuario', None)
    session.pop('tipo_usuario', None)
    return jsonify({'message': 'Sesión cerrada exitosamente'}), 200

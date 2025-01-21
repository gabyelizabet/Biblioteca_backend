from flask import jsonify, request
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
        data = request.json
        user = User.verify_login(data['usuario'], data['contrasena'])
        if user:
            return jsonify({'message': 'Login successful'}), 200
        return jsonify({'message': 'Invalid credentials'}), 401


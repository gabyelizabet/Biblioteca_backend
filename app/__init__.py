from flask import Flask
from flask_cors import CORS
from .routes.book_routes import book_routes
from .routes.user_routes import user_routes
from .models.database import get_db_connection
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

def create_app():
    # Crear la aplicación Flask
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'mi_clave_secreta')

    # Habilitar CORS
    CORS(app)

    # Registrar las rutas (los Blueprints) para los libros y los usuarios
    app.register_blueprint(book_routes)
    app.register_blueprint(user_routes)
    
    #Ruta raiz
    @app.route('/')
    def home():
        return "Bienvenido a la API de Biblioteca"


    return app

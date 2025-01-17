from flask import Flask, jsonify, request, session
from flask_cors import CORS
from models import add_bibliotecario, get_bibliotecario_by_usuario, verify_bibliotecario_password, get_all_books, add_book, get_all_categories, get_all_tags, add_tag_to_book, get_book_by_id

app = Flask(__name__)
CORS(app)
app.secret_key = 'mi_clave_secreta'  # Para manejar sesiones de manera segura


@app.route('/')
def home():
    return jsonify({'message': 'API de Biblioteca está funcionando'}), 200

# Ruta para registrar un bibliotecario
@app.route('/api/bibliotecarios', methods=['POST'])
def register_bibliotecario():
    data = request.json
    nombre = data['nombre']
    apellido = data['apellido']
    email = data['email']
    telefono = data['telefono']
    usuario = data['usuario']
    contrasena = data['contrasena']

    # Validar que todos los campos necesarios están presentes
    required_fields = ['nombre', 'apellido', 'email', 'telefono', 'usuario', 'contrasena']
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Missing required fields'}), 400

    # Registrar al bibliotecario en la base de datos
    add_bibliotecario(nombre, apellido, email, telefono, usuario, contrasena)
    return jsonify({'message': 'Bibliotecario registrado exitosamente!'}), 201

# Ruta para iniciar sesión como bibliotecario
@app.route('/api/bibliotecarios/login', methods=['POST'])
def login_bibliotecario():
    data = request.json
    usuario = data['usuario']
    contrasena = data['contrasena']

    # Obtener el bibliotecario desde la base de datos
    bibliotecario = get_bibliotecario_by_usuario(usuario)

    if not bibliotecario:
        return jsonify({'message': 'Usuario no encontrado'}), 404

    # Verificar la contraseña
    if not verify_bibliotecario_password(bibliotecario['contrasena'], contrasena):
        return jsonify({'message': 'Contraseña incorrecta'}), 401

    # Iniciar sesión (guardar usuario en la sesión)
    session['usuario'] = usuario
    return jsonify({'message': 'Sesión iniciada exitosamente'}), 200

# Ruta para cerrar sesión
@app.route('/api/bibliotecarios/logout', methods=['POST'])
def logout_bibliotecario():
    session.pop('usuario', None)  # Eliminar el usuario de la sesión
    return jsonify({'message': 'Sesión cerrada exitosamente'}), 200

# Ruta para obtener todos los libros
@app.route('/api/books', methods=['GET'])
def get_books():
    books = get_all_books()
    return jsonify(books), 200

# Ruta para obtener un libro por ID
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = get_book_by_id(book_id)
    if book:
        return jsonify(book), 200
    return jsonify({'message': 'Book not found'}), 404

# Ruta para agregar un nuevo libro
@app.route('/api/books', methods=['POST'])
def create_book():
    data = request.json
    titulo = data['titulo']
    isbn = data['isbn']
    autor = data['autor']
    editorial = data['editorial']
    anio_publicacion = data['anio_publicacion']
    cantidad_ejemplares = data['cantidad_ejemplares']
    id_categoria = data['id_categoria']

    add_book(titulo, isbn, autor, editorial, anio_publicacion, cantidad_ejemplares, id_categoria)
    return jsonify({'message': 'Book added successfully!'}), 201

# Ruta para obtener todas las categorías
@app.route('/api/categories', methods=['GET'])
def get_categories():
    categories = get_all_categories()
    return jsonify(categories), 200

# Ruta para obtener todas las etiquetas
@app.route('/api/tags', methods=['GET'])
def get_tags():
    tags = get_all_tags()
    return jsonify(tags), 200

# Ruta para agregar una etiqueta a un libro
@app.route('/api/books/<int:book_id>/tags', methods=['POST'])
def add_tag(book_id):
    data = request.json
    id_etiqueta = data['id_etiqueta']
    add_tag_to_book(book_id, id_etiqueta)
    return jsonify({'message': 'Tag added successfully to the book!'}), 201

if __name__ == '__main__':
    app.run(debug=True)

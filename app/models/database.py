import os
import mysql.connector
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

load_dotenv()

# Configuración de la conexión a la base de datos MySQL
def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    return connection

# Funciones para agregar bibliotecarios y lectores
def add_bibliotecarios(nombre, apellido, email, telefono, usuario, contrasena):
    connection = get_db_connection()
    cursor = connection.cursor()
    bcrypt = Bcrypt()
    hashed_contrasena = bcrypt.generate_password_hash(contrasena).decode('utf-8')
    cursor.execute('''
        INSERT INTO bibliotecarios (nombre, apellido, email, telefono, usuario, contrasena)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (nombre, apellido, email, telefono, usuario, hashed_contrasena))
    connection.commit()
    cursor.close()
    connection.close()

def add_lector(nombre, apellido, email, telefono, matricula, usuario, contrasena):
    connection = get_db_connection()
    cursor = connection.cursor()
    bcrypt = Bcrypt()
    hashed_contrasena = bcrypt.generate_password_hash(contrasena).decode('utf-8')
    cursor.execute('''
        INSERT INTO lectores (nombre, apellido, email, telefono, matricula, usuario, contrasena)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    ''', (nombre, apellido, email, telefono, matricula, usuario, hashed_contrasena))
    connection.commit()
    cursor.close()
    connection.close()

def get_usuario_by_usuario(usuario):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM lectores WHERE usuario = %s', (usuario,))
    usuario_obj = cursor.fetchone()
    if not usuario_obj:
        cursor.execute('SELECT * FROM bibliotecarios WHERE usuario = %s', (usuario,))
        usuario_obj = cursor.fetchone()
    cursor.close()
    connection.close()
    return usuario_obj

def verify_password(hashed_contrasena, contrasena):
    bcrypt = Bcrypt()
    return bcrypt.check_password_hash(hashed_contrasena, contrasena)

# Funciones para obtener libros, categorías, y etiquetas
def get_all_books():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('''
        SELECT libros.id_libro, libros.titulo, libros.isbn, libros.autor, libros.editorial, 
               libros.anio_publicacion, libros.cantidad_ejemplares, categorias.nombre_categoria
        FROM libros
        JOIN categorias ON libros.id_categoria = categorias.id_categoria;
    ''')
    books = cursor.fetchall()
    cursor.close()
    connection.close()
    return books

def get_book_by_id(book_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('''
        SELECT libros.id_libro, libros.titulo, libros.isbn, libros.autor, libros.editorial, 
               libros.anio_publicacion, libros.cantidad_ejemplares, libros.ejemplares_disponibles, categorias.nombre_categoria
        FROM libros
        JOIN categorias ON libros.id_categoria = categorias.id_categoria
        WHERE libros.id_libro = %s;
    ''', (book_id,))
    book = cursor.fetchone()
    cursor.close()
    connection.close()
    return book

def add_book(titulo, isbn, autor, editorial, anio_publicacion, cantidad_ejemplares, id_categoria):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO libros (titulo, isbn, autor, editorial, anio_publicacion, cantidad_ejemplares, ejemplares_disponibles, id_categoria)
        VALUES (%s, %s, %s, %s, %s, %s,%s, %s)
    ''', (titulo, isbn, autor, editorial, anio_publicacion, cantidad_ejemplares, cantidad_ejemplares, id_categoria))
    connection.commit()
    cursor.close()
    connection.close()
"""def add_book(titulo, isbn, autor, editorial, anio_publicacion, cantidad_ejemplares, id_categoria):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO libros (titulo, isbn, autor, editorial, anio_publicacion, cantidad_ejemplares, ejemplares_disponibles, id_categoria)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ''', (titulo, isbn, autor, editorial, anio_publicacion, cantidad_ejemplares, cantidad_ejemplares, id_categoria))
    connection.commit()
    cursor.close()
    connection.close()"""

def get_all_categories():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM categorias;')
    categories = cursor.fetchall()
    cursor.close()
    connection.close()
    return categories

def get_all_tags():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM etiquetas;')
    tags = cursor.fetchall()
    cursor.close()
    connection.close()
    return tags

def add_tag_to_book(id_libro, id_etiqueta):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO libro_etiqueta (id_libro, id_etiqueta)
        VALUES (%s, %s);
    ''', (id_libro, id_etiqueta))
    connection.commit()
    cursor.close()
    connection.close()

def remove_tag_from_book(id_libro, id_etiqueta):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
        DELETE FROM libro_etiqueta
        WHERE id_libro = %s AND id_etiqueta = %s;
    ''', (id_libro, id_etiqueta))
    connection.commit()
    cursor.close()
    connection.close()

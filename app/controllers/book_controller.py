from flask import jsonify, request
from ..models.book import Book

class BookController:
    @staticmethod
    def get_books():
        books = Book.get_all_books()
        return jsonify(books), 200

    @staticmethod
    def get_book(id):
        book = Book.get_book_by_id(id)
        if book:
            return jsonify(book), 200
        return jsonify({'message': 'Book not found'}), 404

    @staticmethod
    def create_book():
        data = request.get_json()     

        # Verifica si los datos requeridos están presentes
        if not all(key in data for key in ['titulo', 'isbn', 'autor', 'editorial', 'anio_publicacion', 'cantidad_ejemplares', 'id_categoria']):
            return jsonify({'message': 'Faltan datos requeridos'}), 400

        Book.add_book(data)       
        return jsonify({'message': 'Libro agregado exitosamente!'}), 201
        
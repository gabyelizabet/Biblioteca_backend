from .database import get_all_books, get_book_by_id, add_book

class Book:
    @staticmethod
    def get_all_books():
        return get_all_books()

    @staticmethod
    def get_book_by_id(book_id):
        return get_book_by_id(book_id)

    @staticmethod
    def add_book(data):
        return add_book(data['titulo'], data['isbn'], data['autor'], data['editorial'], data['anio_publicacion'], data['cantidad_ejemplares'], data['id_categoria'])



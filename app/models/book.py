from .database import get_all_books, get_book_by_id, add_book, add_tag_to_book, get_all_categories, get_all_tags

class Book:
    @staticmethod
    def get_all_books(query=None):
        return get_all_books(query)

    @staticmethod
    def get_book_by_id(book_id):
        return get_book_by_id(book_id)

    @staticmethod
    def add_book(data):
        return add_book(data['titulo'], data['isbn'], data['autor'], data['editorial'], data['anio_publicacion'], data['cantidad_ejemplares'], data['id_categoria'])

    @staticmethod
    def add_book_with_tags(data):
        # Agrega el libro a la base de datos
        book_id = add_book(data['titulo'], data['isbn'], data['autor'], data['editorial'], data['anio_publicacion'], data['cantidad_ejemplares'], data['id_categoria'], data.get('id_etiquetas'))
        
        # Si hay etiquetas, agrega las relaciones en la tabla intermedia
        if 'id_etiquetas' in data and data['id_etiquetas']:
            for etiqueta_id in data['id_etiquetas']:
                add_tag_to_book(book_id, etiqueta_id)
        
        return book_id
    
    @staticmethod
    def get_all_categories(query=None):
        return get_all_categories(query)

    @staticmethod
    def get_all_tags(query=None):
        return get_all_tags(query)

    
    

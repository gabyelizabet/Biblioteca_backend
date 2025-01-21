from flask import Blueprint 
from ..controllers.book_controller import BookController

book_routes = Blueprint('book_routes', __name__)

book_routes.route('/books', methods=['GET'])(BookController.get_books)
book_routes.route('/book/<int:id>', methods=['GET'])(BookController.get_book)
book_routes.route('/api/books', methods=['POST'])(BookController.create_book)

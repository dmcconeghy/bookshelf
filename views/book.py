from flask import render_template
from models import Book

def catalog():
    books = Book.query.all()
    return render_template('catalog.html', books=books)

def book_details(book_id):
    book = Book.query.get(book_id)
    return render_template('book_details.html', book=book)
    
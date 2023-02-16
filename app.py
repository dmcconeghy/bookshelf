import os
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap

from models import db, connect_db, Book
from forms import AddBookByInputForm, AddBookByISBNForm
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.app_context().push()
toolbar = DebugToolbarExtension(app)
Bootstrap(app)

#Flask-WTF requires an encryption key - the string can be anything
app.config['Secret_Key'] = os.environ.get('SECRET_KEY', 'J[.XQ&*i_D$!$%Nn#D&vHInTdDn@nv')
# Necessary for local testing
app.config['WTF_CSRF_ENABLED'] = False


uri = os.environ.get('DATABASE_URL', 'postgresql:///bookshelf')

#PSQL naming conventions changed from postgres to postgresql
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
# db.drop_all()
db.create_all()

@app.route('/')
def home_page():
    return render_template('home.j2')

@app.route('/catalog')
def catalog_page():
    return render_template('catalog.j2', books=Book.query.all())

@app.route('/catalog/<int:book_id>', methods=['GET'])
def book_details_page(book_id):
    return render_template('book.j2', book=Book.query.get(book_id))

@app.route('/catalog/add', methods=['GET', 'POST'])
def add_book_page():
    details_form = AddBookByInputForm()
    isbn_form = AddBookByISBNForm()

    if details_form.validate_on_submit():
        title = details_form.title.data
        author = details_form.author.data
        description = details_form.description.data
        image_url = details_form.image_url.data
        isbn = details_form.isbn.data
        year = details_form.year.data
        book = Book(title=title, author=author, description=description, image_url=image_url, isbn=isbn, year=year)
        db.session.add(book)
        db.session.commit()
        return redirect(f'/catalog/{book.id}')

    if isbn_form.validate_on_submit():
        isbn = isbn_form.isbn.data
        book = Book(isbn=isbn)
        db.session.add(book)
        db.session.commit()
        return redirect(f'/catalog/{book.id}')

    return render_template('add_book.j2', details_form=details_form, isbn_form=isbn_form)
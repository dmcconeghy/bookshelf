import os

from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Book

from forms import AddBookInputForm

app = Flask(__name__)
app.app_context().push()


uri = os.environ.get('DATABASE_URL', 'postgresql:///bookshelf')

if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['WTF_CSRF_ENABLED'] = False
app.config['Secret_Key'] = os.environ.get('SECRET_KEY', 'J[.XQ&*i_D$!$%Nn#D&vHInTdDn@nv')
toolbar = DebugToolbarExtension(app)

connect_db(app)
# db.drop_all()
db.create_all()

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/catalog')
def catalog_page():
    return render_template('catalog.html', books=Book.query.all())

@app.route('/catalog/<int:book_id>', methods=['GET', 'POST'])
def book_details_page(book_id):
    return render_template('book.html', book=Book.query.get(book_id))

@app.route('/catalog/add', methods=['GET', 'POST'])
def add_book_page():
    form = AddBookInputForm()
    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        description = form.description.data
        image_url = form.image_url.data
        isbn = form.isbn.data
        year = form.year.data
        book = Book(title=title, author=author, description=description, image_url=image_url, isbn=isbn, year=year)
        db.session.add(book)
        db.session.commit()
        return redirect(f'/catalog/{book.id}')
    else:
        return render_template('add_book.html', form=form)
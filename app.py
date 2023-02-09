import os

from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Book

app = Flask(__name__)
app.app_context().push()

uri = os.environ.get('DATABASE_URL', 'postgresql:///bookshelf')

if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['Secret_Key'] = os.environ.get('SECRET_KEY', 'default_secret')
toolbar = DebugToolbarExtension(app)

connect_db(app)
# db.drop_all()
db.create_all()

@app.route('/')
def home_page():

    return render_template('home.html')

@app.route('/catalog')
def catalog_page():
    return render_template('catalog.html')
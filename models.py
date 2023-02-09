from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Book(db.Model):
    __tablename__ = 'books'

    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # title = db.Column(db.Text, nullable=False)
    # author = db.Column(db.Text, nullable=False)
    # description = db.Column(db.Text, nullable=False)
    # image_url = db.Column(db.Text, nullable=False)
    # isbn = db.Column(db.Text, nullable=False)
    # year = db.Column(db.Integer, nullable=False)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=True)
    author = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.Text, nullable=True)
    isbn = db.Column(db.Text, nullable=True)
    year = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'{self.title} by {self.author}'

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'description': self.description,
            'image_url': self.image_url,
            'isbn': self.isbn,
            'year': self.year
        }
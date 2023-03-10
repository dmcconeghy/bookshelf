from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms import validators

class AddBookByInputForm(FlaskForm):
    """Form for manually inputting books details."""

    title = StringField("Book Title", [validators.InputRequired()])
    author = StringField("Book Author")
    description = StringField("Book Description")
    image_url = StringField("Book Image URL")
    # image_url = StringField("Book Image URL", [validators.URL()])
    isbn = StringField("Book ISBN")
    year = FloatField("Book Year")

class AddBookByISBNForm(FlaskForm):
    """Form for adding books by ISBN."""

    isbn = StringField("Enter an ISBN")

# TODO: Add a Patch form.
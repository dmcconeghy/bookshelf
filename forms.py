from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField


class AddBookInputForm(FlaskForm):
    """Form for adding books."""

    title = StringField("Book Title")
    Author = StringField("Book Author")
    description = StringField("Book Description")
    image_url = StringField("Book Image URL")
    isbn = StringField("Book ISBN")
    year = FloatField("Book Year")
    
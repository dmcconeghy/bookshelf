# bookshelf

As a former teacher, I have a extensive library. Books and more books! 
As a software development project, I thought it would be fun to create a library web app. 

This project was made using Python, Flask, PSQL, Html, CSS and JavaScript.

The live version of this site is my personal library. 

Core functionality includes:

- Creation of a personal PSQL database 
- Modeling books with SQLAlchemy
- Accepting ISBN from a handheld scanner into a WTF Flask form
- Calling the Google Books API for book details by ISBN
- Saving limited book details into our database per our model  
- Templating with Jinja2 for individual book pages
- Displaying a book's saved Google Books data 

This project has a lengthy todo list:

- Expand book model to include multiple authors, publishers, edition...
- Search functions for internal and external book searches*
- Dockerize the installation and automate deployment 
- Select a component design and integrate tailwind 
- Writing PATCH routing for editing book details
- Select a citation generation package for creating book citations*
- Allow for custom book lists*

### Manual Installation (Temporary)

1. Clone the repo
2. Create a PSQL db "bookshelf" and start your local PSQL server
3. Load a VENV and pip install the requirements. 
4. Flask run the install. 



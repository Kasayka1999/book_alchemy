from flask import Flask, render_template, request, redirect, url_for
from data_models import db, Author, Book
from sqlalchemy import func
import os
from datetime import datetime

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__)) #using abspath to work on from whenever you call the app.py
db_path = os.path.join(basedir, 'data', 'library.sqlite') #using abspath to work on from whenever you call the app.py
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db.init_app(app)

#create tables
#once tables created comment it.
"""with app.app_context():
    db.create_all()
    print("Tables created!")"""

@app.route('/')
def home():
    sort_by = request.args.get('sort', 'title')  # default sort by title
    search_by = request.args.get('search') #search books
    deleted_successfully = request.args.get('deleted_successfully')

    if sort_by == 'author':
        books = Book.query.join(Author).order_by(Author.name).all()
    else:
        books = Book.query.order_by(Book.title).all()

    if search_by:
        books = Book.query.filter(Book.title.ilike(f"%{search_by}%")).all()

    return render_template('home.html', books=books, sort_by=sort_by, deleted_successfully=deleted_successfully)

@app.route('/add_author', methods=['GET','POST'])
def add_author():
  if request.method == "GET":
    return render_template("add_author.html")
  else:
    name = request.form.get('name')
    birthdate = request.form.get('birthdate') #return string
    date_of_death = request.form.get('date_of_death') #return string

    # convert birthdate to python obj dates
    birth_date_obj = datetime.strptime(birthdate, "%Y-%m-%d").date()

    # Convert death date if provided
    death_date_obj = None
    if date_of_death:
        death_date_obj = datetime.strptime(date_of_death, "%Y-%m-%d").date()


    author = Author(
            name = name,
            birth_date = birth_date_obj,
            date_of_death = death_date_obj
        )

    db.session.add(author)
    db.session.commit()
    return render_template(
        "add_author.html",
        message=f"Author added with name: {name}, Birth Date: {birthdate}"
    )


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'GET':
        authors = Author.query.all()
        return render_template('add_book.html', authors=authors)
    else:
        title = request.form.get('name')
        isbn = request.form.get('isbn')
        publication_year = request.form.get('publication_year')
        author_id = request.form.get('author_id')

        #covert str date to obj date
        publication_year_obj = datetime.strptime(publication_year, "%Y-%m-%d").date()

        book = Book(
            title = title,
            isbn = isbn,
            publication_year = publication_year_obj,
            author_id = author_id
        )

        db.session.add(book)
        db.session.commit()

        #re-query authors for the form
        authors = Author.query.all()

        return render_template(
            "add_book.html",
            message=f'Book "{title}" added', authors=authors
        )


@app.route('/book/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    book_to_delete = Book.query.get(book_id)
    if not book_to_delete:
        return {"message": "Book not found"}, 404

    db.session.delete(book_to_delete)
    db.session.commit()
    deleted_successfully = f"Book '{book_to_delete.title}' has been deleted."
    return redirect(url_for('home', deleted_successfully=deleted_successfully))

@app.route('/authors', methods=['GET'])
def authors_list():
    if request.method == 'GET':
        deleted_successfully = request.args.get('deleted_successfully')
        authors_with_count = (
        db.session.query(Author, func.count(Book.id).label('book_count'))
        .outerjoin(Book)
        .group_by(Author.id)
        .order_by(Author.name)
        .all()
    )

    return render_template('authors.html', authors=authors_with_count, deleted_successfully=deleted_successfully)

@app.route('/author/<int:author_id>/delete', methods=['POST'])
def author_delete(author_id):
    if request.method == 'POST':
        author_to_delete = Author.query.get(author_id)
        if not author_to_delete:
            return {"message": "Book not found"}, 404

        db.session.delete(author_to_delete)
        db.session.commit()
        deleted_successfully = f"Author '{author_to_delete.name}' has been deleted."
        return redirect(url_for('authors_list', deleted_successfully=deleted_successfully))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)

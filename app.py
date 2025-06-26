from flask import Flask, render_template, request
from data_models import db, Author, Book
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

    if sort_by == 'author':
        books = Book.query.join(Author).order_by(Author.name).all()
    else:
        books = Book.query.order_by(Book.title).all()

    return render_template('home.html', books=books, sort_by=sort_by)
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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)

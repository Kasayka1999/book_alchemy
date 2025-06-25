from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    birth_date = db.Column(db.Date)
    date_of_death = db.Column(db.Date)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Author id={self.id} name='{self.name}'>"


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.Integer)
    title = db.Column(db.String)
    publication_year = db.Column(db.Date)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Book id={self.id} title='{self.title}' isbn='{self.isbn}'>"

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
    return render_template('home.html')

@app.route('/add_author', methods=['GET','POST'])
def add_author():
  if request.method == "GET":
    return render_template("add_author.html")
  else:
    name = request.form.get('name')
    birthdate = request.form.get('birthdate') #return string
    date_of_death = request.form.get('date_of_death') #return string

    # convert strings to dates
    birth_date_obj = datetime.strptime(birthdate, "%Y-%m-%d").date()
    death_date_obj = datetime.strptime(date_of_death, "%Y-%m-%d").date()

    author = Author(
            name = name,
            birth_date = birth_date_obj,
            date_of_death = death_date_obj
        )

    db.session.add(author)
    db.session.commit()
    return f"Author added: {name}, {birthdate}, {date_of_death}"



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)

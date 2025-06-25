from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from data_models import db
import os
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

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)

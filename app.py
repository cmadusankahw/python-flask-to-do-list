from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# initializing the flask app
app = Flask(__name__)

# setting a secret key to generate csrf token for forms
app.config['SECRET_KEY'] = 'secret-key'

# setting up SQLITE database using SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# importing routes
from routes import *

if __name__ == '__main__':
    app.run(debug=True)




from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agrotech.db'

db = SQLAlchemy(app)
crypt = Bcrypt(app)


login_manager = LoginManager(app)
login_manager.login_view = 'login_manager'




from agrotech import routes
5
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dsakdjlkasjkl'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stld.db'
db = SQLAlchemy(app)

from stld.routes import login
from stld.routes import logout
from stld.routes import controlboard
from stld.routes import createnewlab
from stld.routes import deletelabs
from stld.routes import shutdown
from stld.routes import reset
from stld.routes import status



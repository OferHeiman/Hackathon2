import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Flask Object
app = Flask(__name__)
app.config['SECRET_KEY'] = 'MY SECRET KEY'
app.config['DEBUG'] = True
os.system('export FLASK_APP=run.py')

# Database Connection
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/marketplace"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Representation
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, routes
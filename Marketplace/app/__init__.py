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
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://fgkhfcrgfprvxp:72440aaa640e835a4b93ed360f96255bc012cff4636fd3aabcd2a5d9dd447b09@ec2-54-80-137-25.compute-1.amazonaws.com:5432/d2ld2j9mf29dv4"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/marketplace"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Representation
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, routes
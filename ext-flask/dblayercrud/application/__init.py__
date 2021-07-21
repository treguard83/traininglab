from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@127.0.0.1/gameshopdb" #"sqlite:///data.db"

db = SQLAlchemy(app)
db.create_all()

from application import routes
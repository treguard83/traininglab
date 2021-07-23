from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@127.0.0.1/testdb"
app.config['SECRET_KEY'] = "TEST"

db = SQLAlchemy(app)

class Register(db.Model):
    name = db.Column(db.String(30), nullable=False, primary_key=True)

class RegisterForm(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Submit')

db.create_all()
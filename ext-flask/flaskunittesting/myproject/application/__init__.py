from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@127.0.0.1/testdb"
app.config['SECRET_KEY'] = "TEST"
db = SQLAlchemy(app)
db.create_all()

class Register(db.Model):
    name = db.Column(db.String(30), nullable=False, primary_key=True)

class RegisterForm(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Submit')

db.create_all()

@app.route('/', methods=["GET","POST"])
def home():
    form = RegisterForm()
    if form.validate_on_submit():
        person = Register(name=form.name.data)
        db.session.add(person)
        db.session.commit()
    registrees = Register.query.all()
    return render_template("home.html", registrees=registrees, form=form)
from application import routes
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, DecimalField, SelectField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    dobbo = DateField(format='%Y-%m-%d') # opt arg format='%Y-%m-%d'
    nummo = IntegerField()
    decca = DecimalField(places=2, rounding=None)
    selecta = SelectField('Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    submit = SubmitField('Add Data')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        dobbo = form.dobbo.data
        nummo = form.nummo.data
        decca = form.decca.data
        selecta = form.selecta.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        else:
            return 'Thank you ' + first_name + ' ' + last_name + '. Your DOB is: ' + str(dobbo) + ', you chose number: ' + str(nummo) + ', your decimal was: ' + str(decca) + ', and your selection was ' + str(selecta)

    return render_template('home.html', form=form, message=error)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')
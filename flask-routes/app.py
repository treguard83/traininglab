from flask import Flask
import math

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'This is the home page'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/squirt/<int:sqfrmnum>')
def squirt(sqfrmnum):
    return ('You wanted the square root of {0} which is: {1}'.format(sqfrmnum,int(math.sqrt(sqfrmnum)))) #math.sqrt(sqfrmnum)

if __name__ == "__main__":
    app.run(debug=True)
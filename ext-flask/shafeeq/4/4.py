from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
	return render_template("index.htm")

@app.route("/aboutus")
def aboutus():
	return render_template("aboutus.htm")

@app.route("/services")
def servos():
	return render_template("services.htm")

@app.route("/trainers/shafeeq")
def trainer1():
	return render_template("trainers.htm",name="Shafeeq",address="London")

@app.route("/trainers/paul")
def trainer2():
	return render_template("trainers.htm",name="Paul",address="Swindon")

app.run(debug=True)
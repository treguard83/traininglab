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

@app.route("/trainers/<tname>/<add>")
def trainer1(tname,add):
	color1 = "orange"
	if add == "London":
		color1 = "red"
	if add == "Swindon":
		color1 = "blue"
	if add == "Cardiff":
		color1 = "blue"
	return render_template("trainers.htm",name=tname,address=add,color=color1)

app.run(debug=True)
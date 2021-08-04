from flask import Flask, render_template

app = Flask(__name__)

@app.route("/aboutus")
def aboot():
	return render_template("aboutus.htm")

@app.route("/trainers/shafeeq")
def shafeeq():
	return """
	<a href="http://localhost:5000">Home</a>
	<h2>Shafeeq teaches Python</h2>
	"""

@app.route("/ourservices")
def ourservs():
	return render_template("services.htm")

@app.route("/")
def homepage():
	return """
	<html>
	<center><h1>Welcome to our website</h1></center>
	<br>
	<br>
	<br>
	<a href="http://localhost:5000/aboutus">About Us</a>
	<br>
	<a href="http://localhost:5000/ourservices">Our Services</a>
	</html>
	"""

app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route("/aboutus")
def aboot():
	return """
	<a href="http://localhost:5000">Home</a>
	<h2>We are a training company</h2> <br>
	Our trainers <br>
	Shafeeq <br>
	Leon <br>
	Henry <br>
	Jitesh <br>
	Jane <br>
	Paul <br>
	"""

@app.route("/ourservices")
def ourservs():
	return """
	<a href="http://localhost:5000">Home</a>
	<h2>We provide the following training</h2> <br>
	Java <br>
	Python <br>
	PHP <br>
	JavaScript <br>
	"""

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

app.run()
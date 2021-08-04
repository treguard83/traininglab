from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
	return """
	<html>
	<center><h1>This is my website</h1></center>
	<br>
	<br>
	<center><u>Welcome</u></center>
	<br>
	<center><i>to Nationwide</i></center>
	</html>
	"""

app.run()
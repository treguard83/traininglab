from flask import Flask

app = Flask(__name__)

@app.route("/tree")
def abc():
	return "hello my friends"

@app.route("/nbs")
def boom():
	return "Nationwide"

@app.route("/")
def homepage():
	return "This is my homepage"

app.run()
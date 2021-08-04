from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.htm")

@app.route("/info/<regno>")
def information(regno):
	return render_template("info.htm",rego=regno)

app.run(debug=True)
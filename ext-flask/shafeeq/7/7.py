from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homejames():
	return render_template("index.htm")

@app.route("/addition")
def addingnumbers():
	return render_template("inputform.htm")

@app.route("/processform",methods=['POST'])
def processform():
	return render_template("results.htm",qadata=request.form)

app.run(debug=True)
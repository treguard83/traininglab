from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homejames():
	return render_template("index.htm")

@app.route("/timestable/<tt>")
def index(tt):
	return render_template("timestable.htm",T=int(tt))

@app.route("/abc",methods=['GET','POST'])
def index2():
	return "Hello my friends from GET and POST"

@app.route("/abc",methods=['DELETE'])
def index4():
	return "Hello my friends from DELETE"

app.run(debug=True)
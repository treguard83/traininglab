from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def homejames():
	return render_template("index.htm")

@app.route("/login")
def login():
	return render_template("login.htm")

@app.route("/loginprocess",methods=['POST'])
def processlogindata():
	uname = request.form["username"]
	pword = request.form["password"]
	if uname=="shafeeq" and pword=="abc":
		return redirect("/valid");
	else:
		if uname=="jane" and pword=="tree":
			return redirect("/valid");
	return redirect("/invalid")

@app.route("/invalid")
def invalidlogin():
	return render_template("invalid.htm")

@app.route("/valid")
def validlogin():
	return render_template("valid.htm")

app.run(debug=True)
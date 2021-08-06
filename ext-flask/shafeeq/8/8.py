from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route("/<c>")
def homejames(c):
	res = make_response(render_template("index.htm",color2=c))
	res.set_cookie("MyColor1",c)
	print(c)
	return res

@app.route("/login")
def login():
	return render_template("login.htm")

@app.route("/addition")
def addingnumbers():
	color1 = request.cookies.get("MyColor1")
	print("--->"+request.cookies.get("MyColor1"))
	return render_template("inputform.htm",color2=color1)

@app.route("/processform",methods=['POST'])
def processform():
	color1 = request.cookies.get("MyColor1")
	return render_template("results.htm",qadata=request.form,color2=color1)

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
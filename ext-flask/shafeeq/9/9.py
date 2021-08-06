from flask import Flask, render_template, request, redirect, make_response
app = Flask(__name__)

@app.route("/")
def homejames():
	res = make_response()
	res.set_cookie("name","shafeeq")
	return res

@app.route("/hi")
def hifunction():
	na = request.cookies.get("name")
	return "name was " + na

app.run(debug=True)
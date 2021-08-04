from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<tt>")
def index(tt):
	return render_template("timestable.htm",T=int(tt))

app.run(debug=True)
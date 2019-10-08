import ast, secrets, requests
from flask import Flask, render_template as rend, session


app = Flask(__name__)

with open("bud.txt") as bud_file:
	hlutir = ast.literal_eval(bud_file.read())

app.config['SECRET_KEY'] = secrets.token_hex(256)

@app.route('/karfa')
def checksession():
	output = []
	for x in session["karfa"]:
		output.append(hlutir[x])
	return rend("karfa.html", karfa=output)

@app.route("/add/<hlut>")
def add(hlut):
	karfa = session["karfa"]
	karfa.append(int(hlut))
	session["karfa"] = karfa
	print(session["karfa"])
	return index()

@app.route("/empty")
def empty():
	session["karfa"] = []

	
@app.route('/')
def index():
	if not "karfa" in session:
		print("reset")
		session["karfa"] = []
	return rend("bud.html", title="index", hlutir=hlutir.keys())





@app.errorhandler(404)
def page_not_found(e):
    return rend('404.html')


if __name__ == "__main__":
	app.run(debug=True)
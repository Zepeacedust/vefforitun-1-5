import random, ast
from flask import Flask, render_template as rend
app = Flask(__name__)
with open("frettir.txt") as frett_file:
	frettir = ast.literal_eval(frett_file.read())
@app.route('/')
def index():
	return rend("frettir.html", title="index", frettir=frettir.keys())


@app.route("/<frett>")
def frett(frett):
	if frett in frettir.keys():
		return rend("frett.html", title=frettir[frett][0], content=frettir[frett][1], pic=frett)
	else:
		return page_not_found(None)


@app.errorhandler(404)
def page_not_found(e):
    return rend('404.html')


if __name__ == "__main__":
	app.run(debug=True)
import ast, secrets, requests
from flask import Flask, render_template as rend, session


app = Flask(__name__)

with open("frettir.txt") as frett_file:
	frettir = ast.literal_eval(frett_file.read())

app.config['SECRET_KEY'] = secrets.token_hex(256)

@app.route('/')
def index():
	return '<h3><a href="/on">Set session</a></h3><h3><a href="/off">Delete session</a></h3><h3><a href="/check">Check session</a></h3>'

# Setjum session í gang, 'hilmir' og 'GALVEZ' eru bæði valkvæð gildi sem þú ákveður sjálf / ur
@app.route('/on')
def sessionon():
    session['hilmir'] = 'GALVEZ'
    return '<h3>Session ON</h3><h3><a href="/">Home</a></h3>'

# Eyðum session
@app.route('/off')
def sessionoff():
    if 'hilmir' in session:
        session.pop('hilmir', None)
        return '<h3>Session poped</h3><h3><a href="/">Home</a></h3>'
    else:
        return '<h3>Session was not set</h3><h3><a href="/">Home</a></h3>'

# Athugum hvort session 'hilmir' sé í gangi
@app.route('/check')
def checksession():
    if 'hilmir' in session:
        print(session['hilmir']) # Debug, prentum gildi session í cmd
        return '<h3>ON</h3><h3><a href="/">Home</a></h3>'
    else:
        return '<h3>OFF</h3><h3><a href="/">Home</a></h3>'


if __name__ == "__main__":
	app.run(debug=True)
"""
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
	app.run(debug=True)"""
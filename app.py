import ast, secrets, requests
from flask import Flask, render_template as rend, session, request


app = Flask(__name__)

with open("bud.txt") as bud_file:
    hlutir = ast.literal_eval(bud_file.read())

app.config['SECRET_KEY'] = secrets.token_hex(256)

@app.route('/karfa')
def karfa_p():
    verd = 0
    output = []
    for x in session["karfa"]:
        output.append(hlutir[x])
        verd+=hlutir[x][1]

    return rend("karfa.html", karfa=output, verd=verd)
@app.route('/kaupa',methods = ['POST', 'GET'])
def kaupa():
   if request.method == 'POST':
      result = request.form
      return rend("kaupa.html",result = result)
    
@app.route("/add/<hlut>")
def add(hlut):
    karfa = session["karfa"]
    karfa.append(int(hlut))
    session["karfa"] = karfa
    print(session["karfa"])
    return index()
@app.route("/del/<hlut>")
def rem(hlut):
    karfa = session["karfa"]
    karfa.remove(int(hlut))
    session["karfa"] = karfa
    print(session["karfa"])
    return karfa_p()
@app.route("/eida")
def empty():
    session["karfa"] = []
    return index()

    
@app.route('/')
def index():
    if not "karfa" in session:
        print("reset")
        session["karfa"] = []
        print(hlutir)
    return rend("bud.html", title="index", hlutir=hlutir.items(), karfa=len(session["karfa"]))



@app.errorhandler(404)
def page_not_found(e):
    return rend('404.html')


if __name__ == "__main__":
    app.run(debug=True)
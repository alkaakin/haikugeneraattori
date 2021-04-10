from app import app
from flask import render_template, request, redirect, session
import haikut, users
from os import getenv
#import messages, users -> Pitää siis importtaa ne moduulit, joita tässä erikseen tarvitaan

@app.route("/")
def index():

    return render_template("index.html")
  

@app.route("/login", methods=["GET", "POST"]) 
def login():
    if request.method == "GET":
        return render_template("login.html")
    #oletan että request methodia GET ei tarvii merkitä tähän    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Väärä tunnus tai salasana")
        #huom. pitäisi olla niin, että kirjautumisen jälkeen palaa suoraan takaisin etusivulle
        # ja että kirjautumisen jälkeen etusivulla ei enää ole kirjautumisruutua
        #

@app.route("/haikut")
def haiku():
    list = haikut.get_list()
    return render_template("haikut.html", haikut=list)


@app.route("/new")
def newhaiku():
    return render_template("new.html")

@app.route("/send", methods=["post"])
def send():
    content = request.form["content"]
    if haikut.send(content):
        return redirect("/")
    else:
        return render_template("error.html",message="Viestin lähetys ei onnistunut")


from app import app
from flask import render_template, request, redirect
import haikut
#import messages, users -> Pitää siis importtaa ne moduulit, joita tässä erikseen tarvitaan

@app.route("/")
def index():
    return render_template("index.html")
    #tästä pitää tehdä suoraan kirjautumisruutu, ks. apuja chatmasterista

@app.route("/login", methods=["post", "get"]) #tästä otettu pois get metodeista
#ylläolevaa ei tarvitse muuttaa
def login():
    #if request.method == "GET":
        #return render_template("login.html")
    #oletan että request methodia GET ei tarvii merkitä tähän    
    if request.method == "POST":
        return render_template("error.html",message="Väärä tunnus tai salasana")
        #username = request.form["username"]
        #password = request.form["password"]
        #if users.login(username,password):
            #return redirect("/")
            #eli ylläolevaa varten tulee ottaa käyttöön userstaulu
        #else:
        #return render_template("error.html",message="Väärä tunnus tai salasana")
        #huom. pitäisi olla niin, että kirjautumisen jälkeen palaa suoraan takaisin etusivulle
        # ja että kirjautumisen jälkeen etusivulla ei enää ole kirjautumisruutua
        #

@app.route("/haikut")
def haiku():
    list = haikut.get_list()
    return render_template("haikut.html", haikut=list)
from app import app
from flask import render_template, request, redirect, session
import haikut, users
from os import getenv
from flask import Flask, jsonify, abort, make_response, request, url_for
import random

@app.route("/")
def index():

    return render_template("index.html")
  

@app.route("/login", methods=["GET", "POST"]) 
def login():
    if request.method == "GET":
        return render_template("login.html")   
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Väärä tunnus tai salasana")
       

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/generoi")
def generoi():
    list = haikut.generoi()
    return render_template("generoi.html", random=list)


@app.route("/haikut")
def haiku():
    list = haikut.get_list()
    return render_template("haikut.html", haikut=list)


@app.route("/new")
def newhaiku():
    return render_template("new.html")

@app.route("/send", methods=["post"])
def send():
    nimi = request.form["nimi"]
    genre = request.form["genre"]
    content = request.form["content"]

    if haikut.send(nimi, genre, content):
        return redirect("/")
    else:
        return render_template("error.html",message="Viestin lähetys ei onnistunut")

@app.route("/register", methods=["get","post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Rekisteröinti ei onnistunut")

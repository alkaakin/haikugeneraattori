from db import db
from flask import Flask, jsonify, abort, make_response, request, url_for
import random

def get_list():
    sql = "SELECT * FROM haikut"
    result = db.session.execute(sql)
    return result.fetchall()

def send(nimi, genre, content):
    
    sql = "INSERT INTO haikut (nimi,genre,content) VALUES (:nimi,:genre,:content)"
    db.session.execute(sql, {"nimi":nimi, "genre":genre, "content":content})
    db.session.commit()
    return True

def generoi():
    
    sql="SELECT content, id FROM haikut ORDER BY random() limit 1"
    result = db.session.execute(sql)
    return result.fetchall()
    
def arvostele(arvosana):

     sql = "INSERT INTO haikut (arvosana) VALUES (:arvosana) WHERE haikut.visible = 1"
     db.session.execute(sql, {"arvosana":arvosana})
     db.session.commit()
     sql = "INSERT INTO haikut (visible) VALUES (0) WHERE id = 1"
     db.session.execute(sql, {"id":"0"})
     db.session.commit()
     #ongelmana se, että pitäisi olla tieto haikusta, jota arvostellaan
     #eli tieto id:stä; 
     #id:n avulla haetaan haiku, ja sitten pitäisi myös olla tiedossa haikussa erikseen se,
     #kuinka monta kertaa on arvosteltu

def visible(id2):

    sql = "INSERT INTO haikut (visible) VALUES (1) WHERE id = id2"
    db.session.execute(sql, {"id2":id2})
    db.session.commit()
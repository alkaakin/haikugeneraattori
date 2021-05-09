from db import db
from flask import Flask, jsonify, abort, make_response, request, url_for
import random
import re


def get_list():
    sql = "SELECT * FROM haikut"
    result = db.session.execute(sql)
    return result.fetchall()

def send(nimi, genre, content):
    
    f = "f"
    ratings = 1
    summa = 3
    sql = "INSERT INTO haikut (nimi,genre,content,ratings,sum,arvosana,active) VALUES (:nimi,:genre,:content,:ratings,:summa,:arvosana,:f)"
    db.session.execute(sql, {"nimi":nimi, "genre":genre, "content":content, "ratings":ratings, "summa":summa, "arvosana":'3', "f":f})
    db.session.commit()
    return True

def generoi():
    
    sql="SELECT content, id FROM haikut ORDER BY random() limit 1"
    result = db.session.execute(sql)
    testi = result.fetchall()
    response = merkitse(testi) 
    return testi

def merkitse(lista):

    pattern = '\d+'
    valmis = re.findall(pattern, str(lista))
    valmisint = int(valmis[0])
    t = True
    sql="UPDATE haikut SET active = :t WHERE id = :hid"
    db.session.execute(sql, {"t":t, "hid":valmisint})
    db.session.commit()

def arvostele(arvosana):
    
    avg = int(updateSum(arvosana)) / ratings()
    avg = round(avg, 2)
    f = "f"
    t = "t"
    sql = "UPDATE haikut SET arvosana = :avg, active = :f WHERE active = :t"
    db.session.execute(sql, {"avg":avg, "f":f, "t":t})
    db.session.commit()
     
def ratings():

    t = "t" 
    sql = "SELECT ratings FROM haikut WHERE active = :t"
    result = db.session.execute(sql, {"t":t})
    testi = result.fetchall()
    pattern = '\d+'
    valmis = re.findall(pattern, str(testi))
    #ao. laskee jokaisen t-aktiivisen haikun rating-määrää
    new = int(valmis[0]) + 1     
    sql = "UPDATE haikut SET ratings = :new WHERE active = :t"
    db.session.execute(sql, {"new":new, "t":t})
    db.session.commit()
    return new
    

def updateSum(arvosana):
    t = "t"
    sql = "SELECT sum FROM haikut WHERE active = :t"
    result = db.session.execute(sql, {"t":t})
    testi = result.fetchall()
    pattern = '\d+'
    valmis = re.findall(pattern, str(testi))
    update = int(valmis[0]) + int(arvosana)
    sql = "UPDATE haikut SET sum = :update WHERE active = :t"
    db.session.execute(sql, {"update":update, "t":t})
    db.session.commit()
    return update 

def get_namelist():

    sql = "SELECT * FROM haikut ORDER BY nimi"
    result = db.session.execute(sql)
    return result.fetchall()

def get_genre():
    sql = "SELECT * FROM haikut ORDER BY genre"
    result = db.session.execute(sql)
    return result.fetchall()

def get_rating():
    sql = "SELECT * FROM haikut ORDER BY arvosana DESC"
    result = db.session.execute(sql)
    return result.fetchall()

def get_date():
    sql = "SELECT * FROM haikut ORDER BY id DESC"
    result = db.session.execute(sql)
    return result.fetchall()


from db import db
from flask import Flask, jsonify, abort, make_response, request, url_for
import random
import re
from decimal import Decimal

def get_list():
    sql = "SELECT * FROM haikut"
    result = db.session.execute(sql)
    return result.fetchall()

def send(nimi, genre, content):
    
    f = "f"
    sql = "INSERT INTO haikut (nimi,genre,content,arvosana,active) VALUES (:nimi,:genre,:content,:arvosana,:f)"
    db.session.execute(sql, {"nimi":nimi, "genre":genre, "content":content, "arvosana":'0', "f":f})
    db.session.commit()
    return True

def generoi():
    
    sql="SELECT content, id FROM haikut ORDER BY random() limit 1"
    result = db.session.execute(sql)
    testi = result.fetchall()
    print(testi)
    response = merkitse(testi)
    print(response) 
    return testi

def merkitse(lista):

    pattern = '\d+'
    valmis = re.findall(pattern, str(lista))
    print(valmis)
    valmisint = int(valmis[0])
    print("tässä kaikki trueksi muutettavat " + str(valmisint))
    t = True
    sql="UPDATE haikut SET active = :t WHERE id = :hid"
    db.session.execute(sql, {"t":t, "hid":valmisint})
    db.session.commit()

def arvostele(arvosana):
    
    print(arvosana)
    avg = int(updateSum(arvosana)) / ratings()
    f = "f"
    t = "t"
    print("tässä on keskiarvo" + str(avg))
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
    print("tämä on t-aktiivisen haikun ratingien kokonaismäärä PITÄÄ OLLA VAIN YKSI" + str(valmis))
    new = int(valmis[0]) + 1     #int() argument must be a string, a bytes-like object or a number, not 'CursorResult
    print("tämä on päivitetty ratingien kokonaismäärä" + str(new))
    sql = "UPDATE haikut SET ratings = :new WHERE active = :t"
    db.session.execute(sql, {"new":new, "t":t})
    db.session.commit()
    return new
    #tässä pitää hakea ao. updateCountista 

def updateSum(arvosana):
    t = "t"
    sql = "SELECT sum FROM haikut WHERE active = :t"
    result = db.session.execute(sql, {"t":t})
    testi = result.fetchall()
    print("tässä on database result " + str(testi))
    pattern = '\d+'
    valmis = re.findall(pattern, str(testi))
    print("tässäonvalmissumma " + str(valmis))
    #print(result)
    update = int(valmis[0]) + int(arvosana)
    sql = "UPDATE haikut SET sum = :update WHERE active = :t"
    db.session.execute(sql, {"update":update, "t":t})
    db.session.commit()
    print("tässä päivitetty summa " + str(update))
    return update 

    #tässä pitää päivittää arvosteluiden yhteismäärä

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


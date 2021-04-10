from db import db
from flask import Flask, jsonify, abort, make_response, request, url_for
#tämä ylempi rivi pitää kuulemma importtaa, jos haluaa randomin pythoniin
import random

def get_list():
    sql = "SELECT * FROM haikut"
    result = db.session.execute(sql)
    return result.fetchall()

def send(content):
    #user_id = users.user_id()
    #if user_id == 0:
        #return False
        #tässä vaiheessa siis returnataan aina true
    sql = "INSERT INTO haikut (content) VALUES (:content)"
    db.session.execute(sql, {"content":content})
    db.session.commit()
    return True

def generoi():
    
    
    #sqlcount =  "select count(*) from haikut"
    #muunnos = int(sqlcount) 
    #n = random.randint(0, sqlcount)
    #un= str(n)
    #sql = "select content from haikut where id = (%s)", (n)
    sql="select content from haikut order by random() limit 1"
    result = db.session.execute(sql)
    return result.fetchall()
    #minkä tyyppistä tietoa tämän piäii palattaa?

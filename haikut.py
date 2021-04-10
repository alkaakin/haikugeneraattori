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
    
    sql="select content from haikut order by random() limit 1"
    result = db.session.execute(sql)
    return result.fetchall()
    
    
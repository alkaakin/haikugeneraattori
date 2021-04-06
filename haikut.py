from db import db

def get_list():
    sql = "SELECT * FROM haikut"
    result = db.session.execute(sql)
    return result.fetchall()


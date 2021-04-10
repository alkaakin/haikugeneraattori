from db import db

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
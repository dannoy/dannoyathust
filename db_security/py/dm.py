import pyodbc


CONN = ""
cursor = ""



def connect(server,db,uid,pwd):
    global CONN
    global CURSOR
    sql = 'DRIVER={DM ODBC DRIVER};SERVER=' + server + ';database=' + db + ';UID=' + uid + ';PWD=' + pwd
    CONN = pyodbc.connect(sql)
    CURSOR = CONN.cursor()

def test():
    CURSOR.execute("select * from t1")
    while 1:
        row = CURSOR.fetchone()
        if not row:
            break
        print "col1 %s col2 %s" % (row.COL1,row.COL2)

def insert(v1,v2):
    n = 0
    try:
        n = CURSOR.execute("insert into schemea.sat1(col1,col2) values(?,?)",v1,v2).rowcount
        CONN.commit()
    except :
        n = 0
        #print "error"
    return n

def delete(v1):
    n = 0
    try:
        n = CURSOR.execute("delete from schemea.sat1 where col1=?",v1).rowcount
        CONN.commit()
    except :
        n = 0
        #print "derror"
    return n

def select(v2):
    n = 0
    n = CURSOR.execute("select * from schemea.sat1 where col1=?",v2).rowcount
    return n

def select_all():
    n = 0
    n = CURSOR.execute("select * from schemea.sat1").rowcount
    return n




    

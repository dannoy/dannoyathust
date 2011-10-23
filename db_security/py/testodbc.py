import pyodbc
cnxc = pyodbc.connect('DRIVER={DM ODBC DRIVER};SERVER=localhost;database=DBATEST;UID=SYSDBA;PWD=SYSDBA')
cursor = cnxc.cursor()
cursor.execute("select * from t1")
while 1:
    row = cursor.fetchone()
    if not row:
        break
    print row


    

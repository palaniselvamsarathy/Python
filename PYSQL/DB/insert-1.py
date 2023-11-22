import mysql.connector

dbcon = None
mycur = None

try:
    dbcon = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'SarathY1.',
        database = 'pysql'
    )

    print(dbcon)
    mycur = dbcon.cursor()
    print(mycur)

    st = '''
    INSERT INTO user(uid,uname,ucity)values(%s,%s,%s)
    '''
    content = [(101,'sarathy','wayanad'),(102,'sathish','cbe'),(103,'shaf','blr')]
    mycur.executemany(st,content)
    dbcon.commit()
    print("Data Inserted Successfully")

except mysql.connector.DatabaseError as err:
    if err:
        print(err)

finally:
    if mycur:
        mycur.close()

    if dbcon:
        dbcon.close()
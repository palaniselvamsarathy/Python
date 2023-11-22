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
    CREATE TABLE USER(
    uid int,
    uname varchar(255),
    ucity varchar(32)
    )
    '''
    mycur.execute(st)
    dbcon.commit()
    print('Table Created Successfully')

except mysql.connector.DatabaseError as err:
    if err:
        print(err)

finally:
    if mycur:
        mycur.close()

    if dbcon:
        dbcon.close()
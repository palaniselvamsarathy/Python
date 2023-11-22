import mysql.connector
import requests

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
    response = requests.get('https://dummyjson.com/users')
    user_dict = response.json()
    users_list = user_dict['users']
    data = []

    for user in users_list:
        data.append((user['id'], user['firstName'], user['address']['city'],))
    mycur.executemany(st,data)
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
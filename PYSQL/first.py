import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "SarathY1."
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")



for db in mycursor:
    print(db)

mydb.commit()
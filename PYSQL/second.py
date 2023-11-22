import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "SarathY1."
)

mycursor = mydb.cursor()

hey = mycursor.execute("Show tables")

for db in hey:
    print(db)

mycursor.commit()
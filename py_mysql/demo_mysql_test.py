import mysql.connector
#if this page is executed with no errors, you have the "mysql.connector" module installed.

# mysql connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="mydatabase"
)

print(mydb)

# cursor
mycursor = mydb.cursor()

# create database
# mycursor.execute("CREATE DATABASE mydatabase")

# show database
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)
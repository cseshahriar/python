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

# create table
# mycursor.execute("CREATE TABLE customers(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# alter table
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# insert into table
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")

# Insert Multiple Rows
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "was inserted.")

# Get Inserted ID
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Michelle", "Blue Village")
# mycursor.execute(sql, val)
# mydb.commit()
# print("1 record inserted, ID:", mycursor.lastrowid)

# select from table
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
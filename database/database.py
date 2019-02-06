# -*- coding: utf-8 -*-
import mysql.connector
import getpass

mydb = mysql.connector.connect(
  host=" 128.180.13.95",
  user=getpass.getuser(),
  passwd=getpass.getpass('Password:'),
  database="mydatabase"
)

print("mydb: ", mydb)

mycursor = mydb.cursor()

#Create a database
#mycursor.execute("CREATE DATABASE mydatabase")
    
mycursor.execute("SHOW DATABASES")
print()
print("Database")
print("----------------------------------------")
for x in mycursor:
  print(x)
print("----------------------------------------")
print();

#Create a Table
#mycursor.execute("CREATE TABLE maps (name VARCHAR(255), address VARCHAR(255))")

mycursor.execute("SHOW TABLES")
print("Tables")
print("----------------------------------------")
for x in mycursor:
  print(x)
print("----------------------------------------")
print();



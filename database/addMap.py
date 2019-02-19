# -*- coding: utf-8 -*-
import mysql.connector
import getpass
import sys

if (len(sys.argv) != 2):
    print("Please pass a bitmap file")
    sys.exit()

with open(sys.argv[1], 'rb') as file:
    mBitmap = file.read()
    #TO-DO Base64 encode

if mBitmap != None:
    print ("bitmap not null")
    
mName = input('name: ')
if not mName.isalpha():
    print("Not a name")
    sys.exit()
mLevel = input('level: ')
if not mLevel.isdigit():
    print("Not a name")
    sys.exit()
mAdj = input('name: ')

username = getpass.getuser()
mydb = mysql.connector.connect(
  host="128.180.13.95",
  user=username,
  passwd=getpass.getpass('Password:'),
  database="mydatabase"
)

cursor = mydb.cursor();

sql = "INSERT INTO maps(name, level, bitmap, adjlevels) VALUES(%s, %s, %s, %s)"
val = (mName, mLevel, mBitmap, mAdj)
cursor.execute(sql, val)
mydb.commit();
mydb.close()



# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 09:38:11 2019

@author: rlv220
"""

# -*- coding: utf-8 -*-
import mysql.connector
import getpass
import os
import zlib

username = getpass.getuser()
mydb = mysql.connector.connect(
  host="128.180.13.95",
  user=username,
  passwd=getpass.getpass(),
  database="mydatabase",
  auth_plugin='mysql_native_password'
)

def hint():
    print("Hints:")
    print("----------------------------------------")
    print("(q/Q/Quit/quit/exit/Exit):  Quit")
    print("(c): create table")
    print("(d): drops tables")
    print("(s): show tables")
    print("(m): show list of  maps")
    print("(i): insert")
    print("(u): update table")
    print("(h): display this message")
    
def drop():
    command = input('Are you sure you want to delete tables (y/n): ')
    if command is 'y':
        mycursor.execute("DROP TABLE IF EXISTS maps")
    else:
        return

def insert():
    #mycursor.execute("CREATE TABLE maps (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), level INT, bitmap LONGBLOB, adjlevels VARCHAR(255))")

    name = input('name: ')
    level = input('level: ')
    adjlevels = input('adjacent levels: ')
    bitmap = input("Enter the path of your file: ")

    assert os.path.exists(bitmap), "I did not find the file at, "+str(bitmap)
    blob_value = open(bitmap,'rb').read()
    compressed_data = zlib.compress(blob_value, 9)
    
    print("Hooray we found your map!")
    
    sql = "INSERT INTO maps (name, level, bitmap, adjlevels) VALUES (%s, %s, %s, %s)"
    val = (name, level, compressed_data, adjlevels)
    mycursor.execute(sql, val)
    

hint()

mycursor = mydb.cursor()

while True:
    command = input('~>')
    if command in ['q','Q','quit','Quit','exit','Exit']:
        print("Quitting")
        break
    if command is 'i':
       insert()
       continue;
    if command is 'h':
        hint()
    if command is 'drop':
        print("Dropping Tables")
        drop()
    if command is 'm':
        mycursor.execute("SELECT * FROM maps")
        print("----------------------------------------")
        for x in mycursor:
            print(x)
        print("----------------------------------------")
        print()
    if command is 's':
        mycursor.execute("SHOW TABLES")
        print("Tables")
        print("----------------------------------------")
        for x in mycursor:
            print(x)
        print("----------------------------------------")
        print()
    else:
        try:
            print("trying:  " + command)
            mycursor.execute(command)
            for x in mycursor:
                print(x)
        except:
            continue
            
    
  

# -*- coding: utf-8 -*-
import mysql.connector
import getpass

username = getpass.getuser()
mydb = mysql.connector.connect(
  host="128.180.13.95",
  user=username,
  passwd=getpass.getpass('Password:'),
  database="mydatabase"
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

    
hint()

mycursor = mydb.cursor()

while True:
    command = input('~>')
    if command in ['q','Q','quit','Quit','exit','Exit']:
        print("Quitting")
        break
    if command is 'h':
        hint()
    if command is 'd':
        print("Dropping Tables")
        drop()
    if command is 'm':
        mycursor.execute("SELECT * FROM maps")
        print("----------------------------------------")
        for x in mycursor:
            print(x)
        print("----------------------------------------")
        print();
    if command is 's':
        mycursor.execute("SHOW TABLES")
        print("Tables")
        print("----------------------------------------")
        for x in mycursor:
            print(x)
        print("----------------------------------------")
        print();
    else:
        try:
            mycursor.execute(command);
            for x in mycursor:
                print(x)
            
        except:
            print("Invalid Command")
            
    
  

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
    print("(i): insert")
    print("(u): update table")
    print("(h): display this message")
    
hint()

mycursor = mydb.cursor()
'''
mycursor.execute("SHOW DATABASES")
print()
print("Database")
print("----------------------------------------")
for x in mycursor:
    print(x)
print("----------------------------------------")
print();
'''
'''print(username)
mycursor.execute("SHOW GRANTS FOR 'rlv220'@'%'")
permissions = []

for x in mycursor:
    x

y = ''.join(x)
permissions = y.split(',')
        

print(permissions)
if 'SUPER' in permissions:
    print("YES")
else:
    print("NO")
'''
while True:
    #print(username, ">")
    command = input('~>')
    if command in ['q','Q','quit','Quit','exit','Exit']:
        print("Quitting")
        break
    if command is 'h':
        print("H")
        hint()
    else:
        try:
            mycursor.execute(command);
            for x in mycursor:
                print(x)
            
        except:
            print("Invalid Command")
            
    
  

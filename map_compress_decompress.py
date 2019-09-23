# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:47:39 2019

@author: Raymond
"""
import base64
import zlib
# include standard modules
import getopt, sys

def encrypt_map(filename, file_save_name):
    with open(filename + ".bmp", "rb") as image_file:
        e_string = base64.b64encode(image_file.read())
        file = open(file_save_name +'.txt', 'wb')
        file.write(zlib.compress(e_string, 9))
        file.close()
        
def decrypt_map(filename, file_save_name):
    with open(filename + ".txt", "rb") as image_file:
        decompressed = zlib.decompress(image_file.read())
        e_string = base64.b64decode(decompressed)
        file = open(file_save_name + '.bmp', 'wb')
        file.write(e_string)
        file.close()

# read commandline arguments, first
fullCmdArguments = sys.argv

# - further arguments
argumentList = fullCmdArguments[1:]

print argumentList

if len(argumentList) is 3:
    if argumentList[2] == 'True' or argumentList[2] == 'true':
        print('true')
        encrypt_map(argumentList[0], argumentList[1])
    else:
        print('false')
        decrypt_map(argumentList[0], argumentList[1])



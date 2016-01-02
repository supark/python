"""Write a python program that takes a key(a number from 1 to 26)an input file name, and an output file name from the 
command line and uses the key to encrypt it with a ceaser cipher.  A Ceaser cipher performs modular addition of the key and 
the letter.  If the key is 1 then a->b, b->c, ..., y->z, z->a.  Ignore all the things that aren't the letters from a to z
(simply pass them through) and you will want to put the letters into lower case.  Use the file message1.txt and a key of 7 to
encrypt it.
"""


#!/usr/bin/python

key = input("Please type a key : ")
openfile = raw_input("Please type the file which you want to encrypt : ")
outfile = raw_input("Please type the file name you would like to print to : ")

a = open(openfile, "r")

aa = a.read().lower()

file = open(outfile, "w")

l = list(aa)

finallist = []

for ci in l :
   if ci.isalpha() :  
       ci = ord(ci)+key
       if 123 <= ci :
         ci -= 26 
       ci = chr(ci)
       finallist.append(ci)
       file.write(ci)
   else : 
       finallist.append(ci)
       file.write(ci)

print ''.join(finallist)

file.close()        

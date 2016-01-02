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

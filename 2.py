"""Cato and Junius Brutus are using the cipher to encrypt their communications.  In Latin as well as that vulgar Germanic 
language English the letter 'e' is the most common letter.  't' is the second most common.  Write a python program to count
the numbers of each letter in the message.  (i.e. how common is each symbol) then use that to find the key for the message.
Use the file ceaser1.txt for input.
"""


#!/usr/bin/python

a = open('ceaser1.txt')

file = open("ceaser1result.txt", "w")

aa = a.read()

l = list(aa)

alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

alph = [i for i in alp]
max = 150

for ii in alph :
    co = 0
    co = l.count(ii)    
    print str(ii) + ' has ' + str(co)
    if co > max :
           max = co
           fre = str(ii)
           print 'The most frequency letter is ' + str(ii) 
print

key = ord(fre) - ord('e')
print 'key is ' + str(key)
print

finallist2 = []
 
for ci in l :
   if ci.isalpha() :  
       ci = chr(ord(ci) - key)
       ascii = ord(ci)
       if 123 <= ascii :
         ascii -= 26 
       if 96 >= ascii :
         ascii = 123-(97-ascii)
       ci = chr(ascii)  
       finallist2.append(ci)
       file.write(ci)
   else : 
       finallist2.append(ci)
       file.write(ci)

print ''.join(finallist2)

file.close()        

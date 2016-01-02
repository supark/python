#! /usr/bin/python

"""Question 1
[Say] Write program that takes numbers and writes out their proper names.  It can stop with 1000(i.e. 999 is nine hundred
ninety nine, 42 is forty two.)  Numbers that are out of range (1000 and higher) can just be echoed as numbers.
"""

one = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

two = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]


inputnum = raw_input("Please type a number from 1 to 999.  If you want to finish this program, please type 1000 :\n ")

def Say(strnum):
    num = int(strnum)
    if 0 <= num <= 19:
        return one[num]
    elif 20 <= num <= 99:
        if strnum[-1] == "0":
            return two[int(strnum[0])]
        else:
            return two[int(strnum[0])] + "-" + one[int(strnum[1])]
    elif 100 <= num <= 999:
        secon = num % 100
        firs = num / 100
        if secon == 0:
            return one[firs] + " hundred"
        else:
            return one[firs] + " hundred " + Say(str(secon))

intNum = int(inputnum)

if intNum < 1000:
    print Say(inputnum)


"""Question 2
[unSay] Write a program that takes a written description of a number, (forty-two or forty two) and returns the integer value of it.
"""

three = ["","one","two","three","four","five","six","seven","eight","nine","ten"]

four = ["","","","","","","","","","","","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

inputnum2 = raw_input("Please type a written description of a number from one to nine hundred ninety nine without - :\n")

def unSay(strnum):
    
    strnum2 = strnum.split(' ')
    if strnum in one :
        return str(one.index(strnum2[0]))
    if strnum in two :
        if strnum == 'ten' :
            pass
        return str(two.index(strnum2[0])) + "0"
    if len(strnum2) == 2 and strnum2[1] == 'hundred' :
        return str(one.index(strnum2[0])) + "00"
    

    if len(strnum2) == 3 and strnum2[1] == 'hundred' :
        if strnum2[2] in three :
            return str(one.index(strnum2[0])) + "0" + str(one.index(strnum2[2]))
        if strnum2[2] in four :
            return str(one.index(strnum2[0])) + str(one.index(strnum2[2]))
        if strnum2[2] in two :
            return str(one.index(strnum2[0])) + str(two.index(strnum2[2])) + "0" 
    if len(strnum2) == 4 and strnum2[1] == 'hundred' :
        return str(one.index(strnum2[0])) + str(two.index(strnum2[2])) + str(one.index(strnum2[3]))
    else:
        return str(two.index(strnum2[0])) + str(one.index(strnum2[1])) 
print unSay(inputnum2)


"""Question 3
[Math] Use the Say and unSay programs to do written math.  Handle addition, subtraction and multiplication.  Your program
should take one plus one and return two or six times seven and return forty-two(or forty two).
"""

inputnum3 = raw_input("Please type a written description of addition, subtraction and multiplication.  Please using plus, subtract, and times. And number should be one digit.   For example : one plus one or two subtract one : \n")

def Math(mathh) :
    
    mathhh = mathh.split(' ')
    if mathhh[1] == 'plus' :
        a = mathhh[0]
        a1 = unSay(a)
        a2 = int(a1)
        b = unSay(mathhh[2])
        b1 = int(b)
        result = a2 + b1
        result1 = str(result)
        return (Say(result1))
    if mathhh[1] == 'subtract' :
        a = mathhh[0]
        a1 = unSay(a)
        a2 = int(a1)
        b = unSay(mathhh[2])
        b1 = int(b)
        result = a2 - b1
        result1 = str(result)
        return (Say(result1))
    if mathhh[1] == 'times' :
        a = mathhh[0]
        a1 = unSay(a)
        a2 = int(a1)
        b = unSay(mathhh[2])
        b1 = int(b)
        result = a2 * b1
        result1 = str(result)
        return (Say(result1))

print Math(inputnum3)

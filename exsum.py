#!/usr/bin/python


data1 = '2/15/0'
data2 = '1c'

if data2 == '1c': 
   data2.replace('1c','0/5/0')

data21 = data2.replace('1c','0/5/0')
print data21

data11 = data1.split('/')
data22 = data21.split('/')

print data22

datas1 = [int(i) for i in data11]

datas2 = [int(i) for i in data22]

lsum = datas1[0] + datas2[0]
ssum = datas1[1] + datas2[1]
dsum = datas1[2] + datas2[2]


if dsum >= 12: dnum = dsum % 12; ssum += 1
               

if ssum >= 20: snum = ssum % 20; lsum += 1


print(str(lsum)+ "/" + str(snum) + "/" + str(dnum))

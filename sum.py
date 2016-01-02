#!/usr/bin/python


data1 = '1/2/3'
data2 = '2/18/9'

data11 = data1.split('/')
data22 = data2.split('/')


datas1 = [int(i) for i in data11]

datas2 = [int(i) for i in data22]

lsum = datas1[0] + datas2[0]
ssum = datas1[1] + datas2[1]
dsum = datas1[2] + datas2[2]


if dsum >= 12: dnum = dsum % 12; ssum += 1
               

if ssum >= 20: snum = ssum % 20; lsum += 1


print(str(lsum) + "/" + str(snum) + "/" + str(dnum))


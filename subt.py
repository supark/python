#!/usr/bin/python

data1 = '2/18/9'
data2 = '- 1/2/3 1/2'

data11 = data1.split('/')
data21 = data2.replace('- ','')
data22 = data21.replace(' 1/2','.5')
data23 = data22.split('/')

datas1 = [float(i) for i in data11]
datas2 = [float(i) for i in data23]

lsub = datas1[0] - datas2[0]
ssub = datas1[1] - datas2[1]
dsub = datas1[2] - datas2[2]

flsub = int(lsub)

fssub = int(ssub)

ddsub = str(dsub)
fdsub = ddsub.replace('.5',' 1/2')

print (str(flsub) + "/" + str(fssub) + "/" + fdsub)




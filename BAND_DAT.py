#!/usr/bin/python

#Group two extracted data set into a single file
import fileinput
import numpy as np

rawdata1=[]
rawdata2=[]

for line in fileinput.input('band_31.txt', backup='.bak'):
 rawdata1.append(line)

for line in fileinput.input('Gamma_K.txt', backup='.bak'):
 rawdata2.append(line)

dat=np.loadtxt(rawdata1)
datt=np.loadtxt(rawdata2)
dattt=np.array([[1,2,3,4]])

x=0

for column in dat:
 dummy=datt[x][0]
 if column[0] == dummy:
	dum=np.expand_dims(column,0)
	dattt=np.append(dattt,dum,axis=0)
	x+=1
 if x== datt.shape[0]:
	break

np.savetxt('BAND_31.txt',dattt)


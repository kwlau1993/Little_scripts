#!/usr/bin/python

import fileinput
import numpy as np

rawdata1=[]

for line in fileinput.input('KPOINTS.OUT', backup='.bak'):
 rawdata1.append(line)

dat=np.loadtxt(rawdata1)
dat2=np.array([[1,2,3,4,5,6]])
# a length of 6 to fit KPOINTS.OUT

# Column 1 is x-coordinate, Column 2 is y-coordinate. Use the correct formula to extract the direction
for column in dat:
 if abs(column[1]/(column[2]+0.0000000001)-2)<0.0001:
	dum=np.expand_dims(column,0)
	dat2=np.append(dat2,dum,axis=0)

np.savetxt('Gamma_K.txt',dat2)

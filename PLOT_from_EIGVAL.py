#!/usr/bin/python

import fileinput

# Extract solution by their labels in EIGVAL.OUT

filename='band_31.txt'
g = open(filename,'r+')
dummy=1

for line in fileinput.input('EIGVAL.OUT', backup='.bak'):
 if line.startswith('    31 -'):
	dumdum=[dummy,line]
	for item in dumdum:
		g.write("%s" % item)
	dummy+=1

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

def validar(num, lista):
	for i in lista:
		ctr = 0
		# print('num= ' + str(num) + ' i=' + str(i)) # log
		if (num%i==0 and i!=num):
			print(i)
			ctr =1
			break
	if (ctr == 0): 
		return True
	return False

p = []
maxValor = 32977
cont = 0
for m in range(2, maxValor+1):
	p.append(m)

if (validar(maxValor,p)==True):
	print(str(maxValor) +' é primo ')
else:
	print(str(maxValor) +' NÃO é primo ')
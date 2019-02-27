#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date
from datetime import timedelta

def caluleHoliday(ano):
	#Fonte: ghiorzi.org/portg2.htm
	# CALENDARIO GREGORIANO, valido a partir de 1583
	a = ano//100
	b = ano%19
	c = (a-17)//25
	d = a//4
	e = (a-c)//3
	f = ((a-d-e+(19*b)+15)%30)
	g = f//28
	h = (29//(f+1))
	i = ((21-b)//11)
	j = g*h*i
	k = f-(g*(1-j))
	l = ano//4
	m = (ano+l+k+2-a+d)%7
	n = k-m
	p = (n+40)//44
	q = 3 +p
	r = q//4
	s = n+28-(31*r)
	return date(year=ano, month=q, day=s)

for d in range(1951, 2078+1):
	pascoa 	 = caluleHoliday(d)
	carnaval = date(year=int(pascoa.year), month=int(pascoa.month), day=int(pascoa.day)) + timedelta(days=-47)
	cinzas   = date(year=int(pascoa.year), month=int(pascoa.month), day=int(pascoa.day)) + timedelta(days=-46)
	ramos    = date(year=int(pascoa.year), month=int(pascoa.month), day=int(pascoa.day)) + timedelta(days=-7)
	paixao   = date(year=int(pascoa.year), month=int(pascoa.month), day=int(pascoa.day)) + timedelta(days=-2)
	corpusC  = date(year=int(pascoa.year), month=int(pascoa.month), day=int(pascoa.day)) + timedelta(days=60)
	
	print('Pascoa: ' + str(pascoa)+ ' Carnaval: ' + str(carnaval)+ ' Cinzas: ' + str(cinzas)+ ' Ramos: ' + str(ramos)+ ' Paixao: ' + str(paixao)+  ' Corpus Christi: ' + str(corpusC))
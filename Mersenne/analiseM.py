#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importando Dados dos participantes do grupo e criando uma lista 
print('PASSO 001: Importando Dados...\n----------------------------------------------------------')

# Criando um array com os contatos original
#dados = open('mersenne.txt', 'r').readlines().rstrip()
#lista = str(dados) #.replace("'","").split(',')
lista = []
dados = open('mersenne.txt', 'r')
for l in dados:
    lista.append(l.rstrip().replace(',',''))
dados.close()

cont = 0
for i in lista:
	if cont != 0:
		itemAnterior = str(lista[cont-1])
		dif = int(i) - int(itemAnterior)
		print('Item = ' + str(cont).zfill(2) + ' (2^' + str(i).replace(',','') + ')-1  Ant = ' + str(itemAnterior) + ' Diff = ' + str(dif) )
	else:
		print('Item = ' + str(cont).zfill(2) + ' (2^' + str(i).replace(',','') + ')-1  ')
	cont = cont +1
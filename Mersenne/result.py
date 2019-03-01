#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importando Dados dos participantes do grupo e criando uma lista 
print('PASSO 001: Importando Dados dos participantes do grupo...\n----------------------------------------------------------')

# Criando um array com os contatos original
inf = open('74207281-kInf.txt', 'r').readlines()
sup = open('74207281-kSup.txt', 'r').readlines()
primo = open('74207281-mPrimo.txt', 'r').readlines()

print('Primo...: ' + str(len(list(str(primo).replace("'", "").replace("[","").replace("]","")))))
print('Inferior: ' + str(len(list(str(inf).replace("'", "").replace("[","").replace("]","")))))
print('Superior: ' + str(len(list(str(sup).replace("'", "").replace("[","").replace("]","")))))

# sup = 03035646536278527492714531749781168345565181072725
# inf = 03035646536278527492714531749781168345565181072725
# pri = 18213879217671164956287190498687010073391086436351
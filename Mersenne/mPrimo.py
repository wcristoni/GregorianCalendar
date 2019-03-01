#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

inicio = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
print('INICIO: ' + inicio)

potencia = 74207281
primo = (2 ** potencia) - 1

kInf= ( (primo+1) / 6 ) 
kSup= ( (primo-1) / 6 )

# # Massa de testes
# ps = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719]
# for primo in ps:
# 	kInf= ( (primo+1) / 6 ) 
# 	kSup= ( (primo-1) / 6 )

# 	if ((6*kInf-1) == primo):
# 		print('Primo = ' + str(primo).zfill(10) + ' kInf = ' + str(kInf).zfill(10))
	
# 	if ((6*kSup+1) == primo):
# 		print('Primo = ' + str(primo).zfill(10) + ' kSup = ' + str(kSup).zfill(10))

arq = open(str(potencia) + '-mPrimo.txt', 'w')
arq.write(str(primo))
arq.close()

arq = open(str(potencia) + '-kInf.txt', 'w')
arq.write(str(kInf))
arq.close()

arq = open(str(potencia) + '-kSup.txt', 'w')
arq.write(str(kSup))
arq.close()

print('INICIO: ' + inicio)
print('FINAL.: ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

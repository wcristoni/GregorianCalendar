import collections
import datetime
import os.path

def validar(num):
	return (num**2-2)


inicio = datetime.datetime.now() #.strftime("%Y-%m-%d %H:%M")
print('INICIO: ' + str(inicio))

maxValor = 51
p = []
countInicial = 0
cont = 0
ctl = 0 # controla se eh uma retomada de processamento

fileArray = 'SnAte-'+str(maxValor)+'.txt'
if os.path.exists(fileArray):
	dados = open(fileArray, 'r')

	for l in dados:
		linhaTxt = l.rstrip().split(',')
		linhaTxt.remove(linhaTxt[len(linhaTxt)-1])
		for i in linhaTxt:
			p.append(int(i))
	dados.close()
	ctl = 1

arq = open(fileArray, 'a+')

if (ctl == 0):
	p.append(4)
	arq.write(str(p[0]) + ',\n')
else:
	print('ANALISAR COMO RETOMAR O PROCESSO')
	# ANALISAR COMO RETOMAR O PROCESSO

	# print('ctl: ' + str(ctl))
	# ultimoPrimo = p[len(p)-1]

	# if ( (ultimoPrimo-1)%6==0 ):
	# 	countInicial = (ultimoPrimo-1)/6
	# else:
	# 	countInicial = (ultimoPrimo+1)/6

	# print('ultimoPrimo = ' + str(ultimoPrimo))

# print('countInicial+1 = ' + str(countInicial+1 ))
# print('maxValor+1 = ' + str(maxValor+1))
# cont = (countInicial%1000)
# print('cont = ' + str(cont)) 

ultimoN = 4
for m in range(countInicial+1, maxValor+1): #TODO: Entender pq precisa do +1 para ele exibir o primo da ultima iteracao

	num = validar(ultimoN)
	p.append(num)
	arq.write(str(num) + ',\n')
	ultimoN = num

	# log
	print(' S'+ str(m).zfill(5) + ' Digits = ' + str(len(str(ultimoN))).zfill(30) + ' ' + str(len(set(p))).zfill(20) + ' ' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))

arq.close()

final = datetime.datetime.now() #.strftime("%Y-%m-%d %H:%M")
print('INICIO: ' + str(inicio))
print('FINAL: ' + str(final))
print(str((final-inicio).seconds))

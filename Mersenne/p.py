import collections
import datetime
import os.path

def validar(num, lista):
	ctr = 0
	maior = num//2

	for i in lista:
		#print('num= ' + str(num) + ' i=' + str(i) + ' (maior+1)= ' + str((maior+1))) # log
		if (num%i==0):
			ctr =1
			break
		if (i>(maior+1)):
			break
	if (ctr == 0): 
		return True
	return False

inicio = datetime.datetime.now() #.strftime("%Y-%m-%d %H:%M")
print('INICIO: ' + str(inicio))

maxValor = 15*1000000
p = []
countInicial = 0
cont = 0
ctl = 0 # controla se eh uma retomada de processamento

fileArray = 'primosAte-'+str(maxValor)+'.txt'
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
	p.append(2)
	p.append(3)
	arq.write(str(p[0]) + ',')
	arq.write(str(p[1]) + ',')
else:
	print('ctl: ' + str(ctl))
	ultimoPrimo = p[len(p)-1]

	if ( (ultimoPrimo-1)%6==0 ):
		countInicial = (ultimoPrimo-1)/6
	else:
		countInicial = (ultimoPrimo+1)/6

	print('ultimoPrimo = ' + str(ultimoPrimo))

print('countInicial+1 = ' + str(countInicial+1 ))
print('maxValor+1 = ' + str(maxValor+1))
cont = (countInicial%1000)
print('cont = ' + str(cont)) 

for m in range(countInicial+1, maxValor+1): #TODO: Entender pq precisa do +1 para ele exibir o primo da ultima iteracao
	n1 = '  '
	n2 = '  '
	numInf = (6*m-1)
	numSup = (6*m+1)
	
	if (validar(numInf, p) == True):
		n1 = '-P'
		p.append(numInf)
		arq.write(str(numInf) + ',')

	if (validar(numSup, p) == True):
		n2 = '-P'
		p.append(numSup)
		arq.write(str(numSup) + ',')

	cont = cont+1
	# log
	if (cont==1000):
		cont = 0
		print(str(m).zfill(12) + ' (6*m-1)= ' + str((6*m-1)).zfill(12) + n1 + ' (6*m+1)= ' + str((6*m+1)).zfill(12) + n2  + ' P=' + str(len(p)).zfill(12) + ' ' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
		arq.write('\n')

arq.close()

final = datetime.datetime.now() #.strftime("%Y-%m-%d %H:%M")
print('INICIO: ' + str(inicio))
print('FINAL: ' + str(final))
print(str((final-inicio).seconds))

# diff = []
# c = 0
# for i in p:
# 	c=c+1
# 	ant = p[c-2]
# 	if (i - ant) > 0:
# 		print('Elem: '+str(c).zfill(10) + ' valor: ' + str(i).zfill(10) + ' diff: '+ str(i - ant).zfill(10))
# 		diff.append(i - ant)
# 	else:
# 		print('Elem: '+str(c).zfill(10) + ' valor: ' + str(i).zfill(10) + ' diff: '+ str(0).zfill(10))

# groupBy = collections.Counter(diff)
# print(groupBy)
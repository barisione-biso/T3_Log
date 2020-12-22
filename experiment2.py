'''
NOTA: evitar que imprima lo que envio a consola cuando imprimo 
'''
from buscar import buscar
from bloomFilter import bloomFilter
from  generator import generator
import tracemalloc
import time
import sys

def experiment(N, m, k):
	generator(N)
	tracemalloc.start()
	start = time.time()

	#Crea un vector de bit del filtro de bloom
	file = open("L.txt", "r")
	vector = bloomFilter(m,k)
	b = ""
	for i in file:
		vector.insertar(i.split(" ")[0])
	file.close()

	#Revisa si hay coincidencias
	#consultas: esto debe ir documentado en informe, porque escogimos por ejem hacer N/2 consultas, en donde la mitad estan en el archivo y la otra no.
	#	estan en archivo
	file = open("L.txt", "r") #no esta optimizado. es una propuesta, por eso se abre de nuevo el archivo aqui
	existing_string_max = N // 2
	count = 0
	fp=0
	for i in file:
		if count < existing_string_max:
			#Existing strings
			username=i.split(" ")[0]
		else:  
			#no estan en archivo: al agregar un caracter que no esta en el conjunto de caracteres validos, 
			#estamos seguros de que el string buscado no existe en L.
			username=i.split(" ")[0]+'$' 
		if vector.revisar(username):
			temp = buscar(username)
			print(temp)
			if not temp:
				fp +=1
		count += 1
	file.close()
	#monitor
	current, peak = tracemalloc.get_traced_memory()
	print(f"Current memory usage is "+str(current)+"+ / "+str(10**6)+"MB; Peak was "+str(peak)+" / "+str(10**6)+"MB")
	tracemalloc.stop()
	end = time.time()
	elapsed = end - start
	print(elapsed)
	print(fp)
	return N, elapsed, fp, peak

#Inicializa los parametros de entrada
if __name__ == "__main__":
	if len(sys.argv) == 4:
		N = int(sys.argv[1])
		if N < 0:
			print("Error! N is negative")
			sys.exit()
		m = int(sys.argv[2])
		if m < 0:
			print("Error! m is negative")
			sys.exit()
		k = int(sys.argv[3])
		if k < 0:
			print("Error! k is negative")
			sys.exit()
		experiment(N,m,k)
	else:
		print("Error! params not valids")
		sys.exit()



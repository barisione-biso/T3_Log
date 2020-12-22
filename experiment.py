'''
NOTA: evitar que imprima lo que envio a consola cuando imprimo 
'''
from buscar import buscar
from bloomFilter import bloomFilter
import tracemalloc
import time

tracemalloc.start()
start = time.time()

#Crea un vector de bit del filtro de bloom
file = open("L.txt", "r")
vector = bloomFilter(100,10)
b = ""
for i in file:
    vector.insertar(i.split(" ")[0])
file.close()

#Revisa si hay coincidencias
'''
PENDIENTE: Revisar punto 3.1 del enunciado
'''
print (vector.revisar('holamundo'),buscar('holamundo'))                 #este no esta
print (vector.revisar('EJvtZnOwsdSKUxJ'),buscar('EJvtZnOwsdSKUxJ'))     #este si esta
print (vector.revisar('EJvtZnOwsdSKUxJ2'),buscar('EJvtZnOwsdSKUxJ2'))   #este no deberia estar
print (vector.revisar('EJvtZnOwsdSKU'),buscar('EJvtZnOwsdSKU'))         #este no deberia estar


#monitor
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is "+str(current)+"+ / "+str(10**6)+"MB; Peak was "+str(peak)+" / "+str(10**6)+"MB")
tracemalloc.stop()
end = time.time()
elapsed = end - start
print(elapsed)
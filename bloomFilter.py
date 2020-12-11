import random
import mmh3
import BitVector    #Requiere que la instalen con -> pip3 install BitVector

class bloomFiler:
    #Inicializa las varibales en 0
    m = 0
    k = 0
    s = []          #tambien es h_i
    random.seed(0)  #semilla fija

    #Insertar p a cache
    def insertar(self,p):
        for item in self.s:
            self.v[mmh3.hash(p, item) % self.m] = 1

    #Revisar si p esta en v
    def revisar(self,p):
        for item in self.s:
            if self.v[mmh3.hash(p, item) % self.m] == 0:
                return 0
        return 1

    #Imprime v para depurar
    def printVector(self):
        print(self.v)

    #Crea un filtro
    def __init__(self,m,k):
        self.m=m
        self.k=k
        for i in range(self.k):
            self.s.append(random.randint(0,self.k*10)) #cualquier random
        self.v = BitVector.BitVector(size = self.m)

#Test
#a = bloomFiler(100,10)
#a.insertar('foo')
#print(a.revisar('foo'))
#print(a.revisar('foo2'))
#a.printVector()

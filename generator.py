'''
Generador de listas de correos electronicos aleatorios simples
con formato de salida:
    <String[5-30]>+" "+<String[5-30]>+"@"+<String[5-10]>+<domain>+"\n"
parametros de entrada:
    python3 generator.py <N>
con <N> numero de usuarios generados.
Salida:
    L.txt

Nota: este generador genera String validas sin un patron aparente.
Posibles mejoras:   - agregar un patron entre usuario-email.
                    - nombres de usuarios validos.
                    - agregar mas dominios.

ADVERTENCIA!! ES POSIBLE QUE SALGAN CORREOS O USUARIOS IGUALES.
'''
import string
import random
import sys

#Genera un nombre de usurios y su correo con el formato
class generator:
    random.seed(0)  #por default
    domain = [".com",".cl",".gov",".net",".edu",".org"]
    lenName = 30    #por default
    lenMail = 10    #por default

    #Generador de string
    def randomString(self,lenght):
        a = ""
        for i in range(1,int(random.randrange(3,lenght))):
            a+=random.choice(string.ascii_letters)
        return a

    #Inicializa el generador
    def __init__(self,N=30):
        file = open("L.txt", "w")
        for i in range(N):
            name = self.randomString(self.lenName)
            mail = self.randomString(self.lenName)+"@"+self.randomString(self.lenMail)+self.domain[random.randrange(len(self.domain))]+"\n"
            file.write(name+" "+mail)
        file.close()

#Inicializa los parametros de entrada
if __name__ == "__main__":
    if len(sys.argv) == 2:
        N = int(sys.argv[1])
        if N < 0:
            print("Error! N is negative")
            sys.exit()
    else:
        print("Error! params not valids")
        sys.exit()
    generator(N)


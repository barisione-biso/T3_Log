import os

#Busca un usuario usando grep, retorna verdadero si esta y sino falso
def buscar(username):
    #username = 'BfgHToYfSueoxPSgBHsToacJ2'
    cmd = f'grep "'+username + ' " L.txt'
    #cmd = f"grep ’{username}’ L.txt"
    a = os.system(cmd)
    if a == 0:
        return True
    else:
        return False


#Test
#print(buscar('BfgHToYfSueoxPSgBHsToacJ'))
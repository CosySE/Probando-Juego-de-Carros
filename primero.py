

from random import random


print('''
    Bienvenidos al juego de Carros mas locos del mundo
        ''')
noombres=[]
def nombres():
    cant_jugadores=0
    while True:
        var = input('Introduzca los jugadores ')
        if var == '':
            break
        else:
            noombres.append(var)
            cant_jugadores += 1
    return cant_jugadores
    


def crear_pista(jugadores, tamano):
    pista = []
    for i in range(jugadores):
        pista.append(['-'] * tamano)

    return pista

def mostrar(pista):
    for i in pista:
        print(''.join(i))
        
    
def comenzar_juego(longitud,lista,):
    
    pos = 0
    for n in longitud:
        n[0] = lista[pos]
        pos += 1
    mostrar(longitud)
    while True:
        posicion_actual=0
        for n in longitud:
            posicion_nueva=random(0,20)
            n[posicion_nueva] = lista[pos]
            posicion_nueva = posicion_nueva

        
        

        
    # for c in longitud:
    #     for n in nombres:
    #         c[n]


#print(nombres())
pistaelem = crear_pista(nombres(),10)
print(comenzar_juego(pistaelem,noombres))


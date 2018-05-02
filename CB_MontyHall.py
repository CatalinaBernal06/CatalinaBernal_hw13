import numpy as np
from random import *


def sort_doors(): #ordena las puertas
    lista = ['goat', 'goat', 'car']
    np.random.shuffle(lista)
    return lista


def choose_door(): #escoge una puerta al azar
    choice = np.random.choice([0,1,2])
    return choice

def reveal_door(lista, choice): #revela una puerta donde hay una cabra
    for i in range(len(lista)):
        if((i!=choice) and (lista[i]=='goat')):
            lista[i] = 'GOAT_MONTY'
            return lista
    

def finish_game(lista, choice, change): #finaliza el juego y retorna el premio obtenido
    if(change==False):
        return lista[choice]

    elif(change==True):
        for i in range(len(lista)):
            if((i!=choice) and (lista[i]!='GOAT_MONTY')):
                return lista[i]

#car indica para True o False si el jugador se gano el carro
carT = 0
carF = 0

#iteraciones cuando  el jugador decide cambiar de puerta
for i in range(100):
    change1 = True
    listaT = sort_doors()
    c = choose_door()
    lista_T = reveal_door(listaT, c)
    premio = finish_game(lista_T, c, change1)
    if(premio=='car'):
        carT +=1

#iteraciones cuando el jugador no cambia de puerta
for i in range(100):
    change = False
    listaF = sort_doors()
    c = choose_door()
    lista_F = reveal_door(listaF, c)
    premio2 = finish_game(lista_F, c, change)
    if(premio2 == 'car'):
        carF += 1

prob_true = carT/100.0
print "La probabilidad de obtener el premio cuando hubo cambio de puerta es " + str(prob_true)

prob_false = carF/100.0
print "La probabilidad de obtener el premio cuando no hubo cambio de puerta es " + str(prob_false)


#luego de varias pruebas, es conveniente que el jugador cambie de puerta (probabilidad mayor)


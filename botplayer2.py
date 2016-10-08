import numpy
from cliente_alumnos import posicion
global posicionActual

def escoger_movimiento( amenazas ):
    ambos = ambos.strip().split(':')
    amenaza = ambos[0].strip().split('-')
    cuadrante = ambos[1].strip().split('-')
    del amenaza[0]
    movimiento_x = ""
    movimiento_y = ""
    return movimiento_x + "," + movimiento_y

def escoger_disparo( amenazas ):
    ambos = ambos.strip().split(':')
    amenaza = ambos[0].strip().split('-')
    cuadrante = ambos[1].strip().split('-')
    del amenaza[0]
    
    disparo_x = ""
    disparo_y = ""
    return disparo_x + "," + disparo_y

posicionActual = dict()




#Si la posicion es 0 o 9 estamos en una esquina
#en estos puntos distintos cuadrantes y se pierden algunos



##Disparo:
##  -  si 1 cuadrante tiene a todos los wnes y si hay 2 grados de amenaza
##iguales, disparar a eso, 100% chance de golpear.
##  - si hay 2 cuadrantes con jugadores, elegir el que tenga mayor jugadores
##y disparar a la amenaza existida(o mas repetida).
##  - seguir la misma logica para 3 y 4 cuadrantes.
##condiciones para cuando estas en los bordes, se elminan cuadrantes en estos casos

##cuando esta en una esquina y se pierde un cuadrante, entrega 0



##movimiento:
##    - si no hay amenaza, revisar cuadrantes y moverse a donde hay menor cantidad
##de enemigos. (intentar no chocar)





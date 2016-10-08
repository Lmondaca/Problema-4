import numpy
from cliente_alumnos import posicion

def escoger_movimiento(amenazas):
    movimiento_x = ""
    movimiento_y = "" 
    return movimiento_x + "," + movimiento_y    
def escoger_disparo(amenazas):
	a = amenazas.split(":")
    amenaza = a[0].split("-") # Lista de amenazas [a, g1, g2, g3, gn]
    del amenaza[0] # Lista de amenazas [g1, g2, g3, gn]
    cuadrante = a[1].split("-") # Lista de cuadrantes [c1, c2, c3, c4]
    disparo_x = ""
    disparo_y = ""
    return disparo_x + "," + disparo_y

# global posiciones = {} # LLave = N° de turno, Valor = lista de 2 elementos, Posicion (lista con 2 elementos) y amenazas.
#Criterios de disparo
#Criterios de movimiento 

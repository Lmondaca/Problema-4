import numpy
import random
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
	count = 0
    ambos = ambos.strip().split(':')
    amenaza = ambos[0].strip().split('-') #Lista de amenzas [g1, g2, g3, gn]
    cuadrante = ambos[1].strip().split('-') #Lista de cuadrantes [c1, c2, c3, c4]    
    del amenaza[0]
    amenaza.sort()
    c1 = cuadrante[0] #Cuadrantes en valores individuales 
    c2 = cuadrante[1]
    c3 = cuadrante[2]
    c4 = cuadrante[3]
    if (c1 == c2 == c3 == 0): # Todos los enemigos estan en un cuadrante
    	while count < len(amenaza):
    		if amenaza[c] == amenaza[c+1]:
    			disparo_x = "0"
    			if amenaza[c] == "1":
    				disparo_y = random.choice("4", "5")
    				break 
    			elif amenaza[c] == "2":
    				disparo_y = random.choice("2", "3")
    				break
    			else:
    				disparo_y = "1"
    				break
    		else:
    			c += 1
    elif (c1 == c2 == c4 == 0): # Todos los enemigos estan en un cuadrante
    	while count < len(amenaza):
    		if amenaza[c] == amenaza[c+1]:
    			disparo_y = "0"
    			if amenaza[c] == "1":
    				disparo_x = random.choice("-4", "-5")
    				break
    			elif amenaza[c] == "2":
    				disparo_x = random.choice("-3", "-2")
    				break
    			else:
    				disparo_x = "-1"
    				break
    		else:
    				c += 1
    elif (c1 == c3 == c4 == 0): # Todos los enemigos estan en un cuadrante
    	while count < len(amenaza):
    		if amenaza[c] == amenaza[c+1]:
    			disparo_x = "0"
    			if amenaza[c] == "1":
    				disparo_y = random.choice("-4", "-5")
    				break
    			elif amenaza[c] == "2":
    				disparo_y = ranodm.choice("-3", "-2")
    				break
    			else:
    				disparo_y = "-1"
    				break
    		else:
    			c += 1
    elif (c2 == c3 == c4 == 0): # Todos los enemigos estan en un cuadrante
    	while count < len(amenaza):
    		if amenaza[c] == amenaza[c+1]:
    			disparo_y = "0"
    			if amenaza[c] == "1":
    				disparo_x = random.choice("4", "5")
    				break
    			elif amenaza[c] == "2":
    				disparo_x = random.choice("2", "3")
    				break
    			else:
    				disparo_x = "1"
    		else:
    			c += 1  #Cambiar todo esto a funcion 
    	
    #disparo_x = ""
    #isparo_y = ""
    return disparo_x + "," + disparo_y

posicionActual = dict()




#Si la posicion es 0 o 9 estamos en una esquina
#en estos puntos distintos cuadrantes y se pierden algunos



##Disparo:
##  -  si 1 cuadrante tiene a todos los wnes y si hay 2 grados de amenaza
##iguales, disparar a eso, 100% chance de golpear, Hecho!
##  - si hay 2 cuadrantes con jugadores, elegir el que tenga mayor jugadores
##y disparar a la amenaza existida(o mas repetida).
##  - seguir la misma logica para 3 y 4 cuadrantes.
##condiciones para cuando estas en los bordes, se elminan cuadrantes en estos casos

##cuando esta en una esquina y se pierde un cuadrante, entrega 0



##movimiento:
##    - si no hay amenaza, revisar cuadrantes y moverse a donde hay menor cantidad
##de enemigos. (intentar no chocar)







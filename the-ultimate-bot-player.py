import numpy
import random
from cliente_alumnos import posicion
global posicionActual = list(posicion) # Lista de enteros
def escoger_movimiento( amenazas ):
    global posicionActual # Usar la posicion inicial
    # inserte aqui el area de los cuadrantes o el llamada a funcion del area
    grados,cuadrantes=amenazas.strip().split(':')
    grados=grados.split('-') #el primer elemento es 'a'
    cuadrantes=cuadrantes.split('-')
    cuadrantes=map(int, cuadrantes)
    minc=min(cuadrantes)
    if minc == cuadrantes[0]:
        if cuadrantes[1]<cuadrantes[2] and cuadrantes[1]<=cuadrantes[0]:

    if minc == cuadrantes[1]:
        if cuadrantes[2]<cuadrantes[3]:
        
    if minc == cuadrantes[2]:
        if cuadrantes[3]< cuadrantes[0]
        movimiento_y='1'
    elif minc ==cuadrantes[1]:
        movimiento_x='-1'
    elif minc==cuadrantes[2]:
        movimiento_y='-1'
    elif minc==cuadrantes[3]:
        movimiento_x='1'
    
    
    movimiento_x = ""
    movimiento_y = ""
    global posicionActual = [global posicionActual[0]+ int(movimiento_x), global posicionActual[1]+ int(movimiento_y)] # No estoy seguro si el orden x,y está bien puesto
    global posicionActual = periodico(global posicionActual) 
return movimiento_x + "," + movimiento_y

def escoger_disparo( amenazas ):
    ambos = ambos.strip().split(':')
    amenaza = ambos[0].strip().split('-') #Lista de amenzas [g1, g2, g3, gn]
    cuadrante = ambos[1].strip().split('-') #Lista de cuadrantes [c1, c2, c3, c4]    
    del amenaza[0]
    amenaza.sort()
    c1 = cuadrante[0] #Cuadrantes en valores individuales 
    c2 = cuadrante[1]
    c3 = cuadrante[2]
    c4 = cuadrante[3]
    if   c1 != "0" and (c2 == c3 == c4 == "0"):
        disparo_x, disparo_y = disparo_seguro(amenaza, "1")
    elif c2 != "0" and (c1 == c3 == c4 == "0"):
        disparo_x, disparo_y = disparo_seguro(amenaza, "2")
    elif c3 != "0" and (c1 == c2 == c4 == "0"):
        disparo_x, disparo_y = disparo_seguro(amenaza, "3")
    elif c4 != "0" and (c1 == c2 == c2 == "0"):
        disparo_x, disparo_y = disparo_seguro(amenaza, "4")





    return disparo_x + "," + disparo_y

def disparo_seguro(amenaza, cuadrante): # Recibe el cuadrante y la lista de amenzas ordenadas, hecho para no poner todo esto en la funcion escoger_disparo
    count = 0
    if cuadrante == "1": # Todos los enemigos estan en cuadrante 1
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
                c += 1  
    elif cuadrante == "2": # Todos los enemigos estan en cuadrante 2
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
                c +=1   
    elif cuadrante == "3": # Todos los enemigos estan en cuadrante 3
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
    else:
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
    return disparo_x, disparo_y         
def periodico(coordenada): #Evita que la posicion que guardamos se "salga" del tablero, se le da una lista
    Tamanno = 5 #Se asume que el tamaño del tablero es de 5 pues es 1v1 cambiar para gran final, si no es 1v1 preguntar a los ayudantes
     if coordenada[0] >= Tamanno:
        coordenada[0] = coordenada[0] - Tamanno
     if coordenada[1] >= Tamanno:
        coordenada[1] = coordenada[1] - Tamanno
    return [coordenada[0], coordenada[1]] 
def disparar(amenaza, cuadrante):
# funcion para disparos no 100% real    


#Si la posicion es 0 o 9 estamos en una esquina
#en estos puntos distintos cuadrantes y se pierden algunos



##Disparo:
##  - si hay 2 cuadrantes con jugadores, elegir el que tenga mayor jugadores
##y disparar a la amenaza existida(o mas repetida).
##  - seguir la misma logica para 3 y 4 cuadrantes.
##condiciones para cuando estas en los bordes, se elminan cuadrantes en estos casos
##cuando esta en una esquina y se pierde un cuadrante, entrega 0


##movimiento:
##    - si no hay amenaza, revisar cuadrantes y moverse a donde hay menor cantidad
##de enemigos. (intentar no chocar)
# ocupar la posición inicial para calcular la consentracion de jugadores respecto al area de cada caudrante
## en concentracion poner un if si el area del cuadrante es 0 -- ZeroDivisionError o simplemente skipearlo

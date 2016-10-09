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
    num_Jugadores = sum(cuadrantes)+1 #Calcula el numero de jugadores para determianr el tamanio del tablero
    if num_Jugadores <= 5:
        Tablero = 11 #Va del 0 al 10
    elif num_Jugadores <= 10:
        Tablero = 15 #Va del 0 al 14
    else:
        Tablero = 20 #Va del 0 al 19


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
    global posicionActual = periodico(global posicionActual, Tablero)

    return movimiento_x + "," + movimiento_y

def escoger_disparo( amenazas ):
    ambos = ambos.strip().split(':')
    amenaza = ambos[0].strip().split('-') #Lista de amenzas [g1, g2, g3, gn]
    cuadrante = ambos[1].strip().split('-') #Lista de cuadrantes [c1, c2, c3, c4]    
    del amenaza[0]
    num_Jugadores = sum(map(int,cuadrante)) #Calcula el numero de jugadores para determianr el tamanio del tablero
    if num_Jugadores <= 5:
        Tablero = 11 #Va del 0 al 10
    elif num_Jugadores <= 10:
        Tablero = 15 #Va del 0 al 14
    else:
        Tablero = 20 #Va del 0 al 19




    amenaza.sort()
    c1 = cuadrante[0] #Cuadrantes en valores individuales 
    c2 = cuadrante[1]
    c3 = cuadrante[2]
    c4 = cuadrante[3]
    
    if len(amenaza) == 0:  #Cambio en el orden, si no hay amenazas no es necesario ver todo lo siguiente
        disparo_x, disparo_y = "0", "1" # R.I.P
    elif c1 != "0" and (c2 == c3 == c4 == "0"):




        disparo_x, disparo_y = disparo_seguro(amenaza, "1")
    elif c2 != "0" and (c1 == c3 == c4 == "0"):
        disparo_x, disparo_y = disparo_seguro(amenaza, "2")
    elif c3 != "0" and (c1 == c2 == c4 == "0"):
        disparo_x, disparo_y = disparo_seguro(amenaza, "3")
    elif c4 != "0" and (c1 == c2 == c2 == "0"):
        disparo_x, disparo_y = disparo_seguro(amenaza, "4") 
    elif (0 in posicionActual) or ((Tablero-1) in posicionActual):
        disparo_x,disparo_y = bordes(amenaza,Tablero,cuadrante) #La funcion bordes esta en proceso, la subo para que me corrijan si falle
        #dejare las funciones que utiliza mas abajo, luego de las indicaciones que anotamos
    




    elif (c1 != "0") and (c2 != "0") and (c3 != "0") and (c4 != "0"):
        cuadrante_int = map(int, cuadrante)
        max_cuadrante = max(cuadrante_int)





    return disparo_x + "," + disparo_y

def disparo_seguro(amenaza, cuadrante): # Recibe el cuadrante y la lista de amenzas ordenadas, hecho para no poner todo esto en la funcion escoger_disparo


    c = 0 #No existia la variable
    ## REVISAR EN CASO DE QUE AMENAZAS NO SE REPITAN
    if cuadrante == "1": # Todos los enemigos estan en cuadrante 1
        while c < len(amenaza):
            if amenaza[c] == amenaza[c+1]:
                disparo_y = "0"
                if amenaza[c] == "1":
                    disparo_x = random.choice(["4", "5"])
                    break
                elif amenaza[c] == "2":
                    disparo_x = random.choice(["2", "3"])




                    break
            elif amenaza[c] == "3":
                disparo_x = "1"
                break    
            else:
                c += 1  
    elif cuadrante == "2": # Todos los enemigos estan en cuadrante 2
        while c < len(amenaza):
            if amenaza[c] == amenaza[c+1]:
                disparo_x = "0"
                if amenaza[c] == "1":
                    disparo_y = random.choice(["-4", "-5"])
                    break
                elif amenaza[c] == "2":
                    disparo_y = ranodm.choice(["-3", "-2"])




                    break
            elif amenaza[c] == "3":
                disparo_y = "-1"
                break
                    
            else:
                c +=1   
    elif cuadrante == "3": # Todos los enemigos estan en cuadrante 3
        while c < len(amenaza):
            if amenaza[c] == amenaza[c+1]:
                disparo_y = "0"
                if amenaza[c] == "1":
                    disparo_x = random.choice(["-4", "-5"])
                    break
                elif amenaza[c] == "2":
                    disparo_x = random.choice(["-3", "-2"])




                    break
            elif amenaza[c] == "3":
                disparo_x = "-1"
                break
            else:
                c += 1
    else: #Todos los enemigos estan en cuadrante 4
        while c < len(amenaza):
            if amenaza[c] == amenaza[c+1]:
                disparo_x = "0"
                if amenaza[c] == "1":
                    disparo_y = random.choice(["4", "5"])
                    break 
                elif amenaza[c] == "2":
                    disparo_y = random.choice(["2", "3"])




                    break
            elif amenaza[c] == "3":
                disparo_y = "1"
                break
                    
            else:
                c += 1
    return disparo_x, disparo_y
def periodico(coordenada, Tamanno): #Evita que la posicion que guardamos se "salga" del tablero, se le da una lista
    if coordenada[0] >= Tamanno:
        coordenada[0] = Tamanno - coordenada[0]
    if coordenada[1] >= Tamanno:
        coordenada[1] = Tamanno - coordenada[1]
    return [coordenada[0], coordenada[1]]
     
def disparar(amenaza, cuadrante): #Disparo no 100% real (lista de amenzas string, cuadrante con mas enemigos int)  
    cuenta = 0
    amenaza_1 = 0
    amenaza_2 = 0
    while cuenta <= len(amenaza):
        if   amenaza[cuenta] == 1:
            amenaza_1 += 1
            cuenta += 1
        elif amenaza[cuenta] == 2:
            amenaza_2 += 1
            cuenta += 1
        
    if 3 in amenaza:
        if cuadrante == 1:
            disparo_x = "1"
            disparo_y = "0"
            return disparo_x, disparo_y
        elif cuadrante == 2:
            disparo_x = "0"
            disparo_y = "-1"
            return disparo_x, disparo_y
        elif cuadrante == 3:
            disparo_x = "-1"
            disparo_y = "0"
            return disparo_x, disparo_y
        else:
            disparo_x = "0"
            disparo_y = "1"
            return disparo_x, disparo_y
    elif amenaza_2 >= amenaza_1:
        if   cuadrante == 1:
            disparo_x = random.choice("3", "2")
            disparo_y = "0"
            return disparo_x, disparo_y
        elif cuadrante == 2:
            disparo_x = "0"
            disparo_y = random.choice("-2", "-3")
            return disparo_x, disparo_y
        elif cuadrante == 3:
            disparo_x = random.choice("-2", "-3")
            disparo_y = "0"
            return disparo_x, disparo_y
        else:
            disparo_x = "0"
            disparo_y = random.choice("2", "3")
            return disparo_x, disparo_y
    else:
        if   cuadrante == 1:
            disparo_x = random.choice("5", "4")
            disparo_y = "0"
            return disparo_x, disparo_y
        elif cuadrante == 2:
            disparo_x = "0"
            disparo_y = random.choice("-5", "-4")
            return disparo_x, disparo_y
        elif cuadrante == 3:
            disparo_x = random.choice("-5", "-4")
            disparo_y = "0"
            return disparo_x, disparo_y
        else:
            disparo_x = "0"
            disparo_y = random.choice("5", "4")
            return disparo_x, disparo_y



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


##Esta es mi idea de como podria funcionar el bot al estar en los bordes
##Las siguientes funciones hacen lo mismo tecnicamente, X0 se refiere a disparos verticales e
##Y0 se refiere a disparos horizontales, se difencian en signos dentro de los choice, por eso
##las separe como arriba/abajo y derecha/izquierda

def disp_X0_abajo(cercania1,cernacia2_3,cercania4_5): 
    disparo_x = '0'
    if cercania1 > 0: #si hay alguien a 1 cuadro de distancia nos la jugamos
        disparo_y = '-1'
    elif cercania2_3 > cercania4_5:# si hay mayor amenazas a 2/3 cuadros
        disparo_y = random.choice(['-2','-3'])
    else:
        disparo_y = random.choice(['-4','-5'])
    return disparo_x,disparo_y

def disp_Y0_derecha(cercania1,cernacia2_3,cercania4_5):
    disparo_y = '0'
    if cercania1 > 0:
        disparo_x = '1'
    elif cercania2_3 > cercania4_5:
        disparo_x = random.choice(['2','3'])
    else:
        disparo_x = random.choice(['4','5'])
    return disparo_x,disparo_y

def disp_X0_arriba(cercania1,cernacia2_3,cercania4_5):
    disparo_x = '0'
    if cercania1 > 0:
        disparo_y = '1'
    elif cercania2_3 > cercania4_5:
        disparo_y = random.choice(['2','3'])
    else:
        disparo_y = random.choice(['4','5'])
    return disparo_x,disparo_y

def disp_Y0_izquierda(cercania1,cernacia2_3,cercania4_5):
    disparo_y = '0'
    if cercania1 > 0:
        disparo_x = '-1'
    elif cercania2_3 > cercania4_5:
        disparo_x = random.choice(['-2','-3'])
    else:
        disparo_x = random.choice(['-4','-5'])
    return disparo_x,disparo_y

def bordes(amenaza,Tablero,cuadrante):
    cercania1 = amenaza.count('3')
    cercania2_3 = amenaza.count('2')
    cercania4_5 = amenaza.count('1')
    c1 = int(cuadrante[0])
    c2 = int(cuadrante[1])
    c3 = int(cuadrante[2])
    c4 = int(cuadrante[3])
    if posicionActual[0] == 0: #Cuando se encuentra en el lado izquierdo del tablero
        if posicionActual[1] == 0: #Esquina superior izquierda
            if c3 != 0: #c3 es solamente la linea debajo del bot, si hay amenazas tenemos mas chances de golpear
                disparo_x,disparo_y = disp_X0_abajo(cercania1,cernacia2_3,cercania4_5)
                
            else: #se hace lo mismo pero para el eje x en caso de que en c3 no hayan amenazas
                disparo_x,disparo_y = disp_Y0_derecha(cercania1,cernacia2_3,cercania4_5)
                
        elif posicionActual[1] == (Tablero-1):
            if c4 != 0: #En este caso el c4 es solo una fila, si hay amenazas la jugamos ahi
                disparo_x,disparo_y = disp_Y0_derecha(cercania1,cernacia2_3,cercania4_5)

            else:
                disparo_x,disparo_y = disp_X0_arriba(cercania1,cernacia2_3,cercania4_5)
                
        elif posicionActual[1] != 0: #Lado izquierdo del tablero
            if c3 != 0: #totalmente lo mismo que arriba
                disparo_x,disparo_y = disp_X0_abajo(cercania1,cernacia2_3,cercania4_5)
                
            elif c1 > c4: # se sigue la misma logica, solo que se comparan los dos cuadrantes sobrantes
                disparo_x,disparo_y = disp_X0_arriba(cercania1,cernacia2_3,cercania4_5)
                #se dispara hacia arriba en caso de que hayan mas enemigos arriba
            else:
                disparo_x,disparo_y = disp_Y0_derecha(cercania1,cernacia2_3,cercania4_5)
                #se dispara hacia la derecha en caso de que hayan mas enemigos en el cuarto cuadrante
        

    return disparo_x,disparo_y




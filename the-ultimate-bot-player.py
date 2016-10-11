# coding=iso-8859-1 
import numpy
import random

def escoger_movimiento( amenazas ):
    grados,cuadrantes=amenazas.strip().split(':')
    grados=grados.split('-') #el primer elemento es 'a'
    cuadrantes=cuadrantes.split('-')
    cuadrantes=map(int, cuadrantes)
    c1 = cuadrantes[0]
    c2 = cuadrantes[1]
    c3 = cuadrantes[2]
    c4 = cuadrantes[3]
    am2 = grados.count('2')
    minC = min(cuadrantes)
    maxC = max(cuadrantes)
    movimiento_x, movimiento_y = '0', '0'
    if '3' in grados:
        if 0 in cuadrantes:
            if c1 == 0:
                movimiento_x = random.choice(['-2','-3'])
            elif c2 == 0:
                movimiento_y = random.choice(['-2','-3'])
            elif c3 == 0:
                movimiento_x = random.choice(['2','3'])
            else:
                movimiento_y = random.choice(['2','3'])
        elif minC == c1:
            movimiento_x = random.choice(['-2','-3'])
        elif minC == c2:
            movimiento_y = random.choice(['-2','-3'])
        elif minC == c3:
            movimiento_x = random.choice(['2','3'])
        else:
            movimiento_y = random.choice(['2','3'])
    elif '3' not in grados and am2 == 0:
        if c1 == maxC and c2 == minC:
            movimiento_y = random.choice(['1','2','3'])
        elif c1 == maxC and c3 == minC:
            movimiento_x = random.choice(['1','2','3'])
        elif c2 == maxC and c3 == minC:
            movimiento_x = random.choice(['-1','-2','-3'])
        elif c3 == maxC and c4 == minC:
            movimiento_y = random.choice(['-1','-2','-3'])
        else:
            movimiento_x = random.choice(['2','3'])
    else:
        if c1 == maxC:
            movimiento_x = '-1'
        elif c2 == maxC:
            movimiento_y = '-1'
        elif c3 == maxC:
            movimiento_x = '1'
        else:
            movimiento_y = '1'



    if movimiento_x == '':
        movimiento_x = '0'
    elif movimiento_y == '':
        
        movimiento_y == '0'
    return movimiento_x + "," + movimiento_y

def escoger_disparo( amenazas ):
    ambos = amenazas.strip().split(':') #:V
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
    else:
        disparo_x,disparo_y = disparar(amenaza,cuadrante) 
        
    return disparo_x + "," + disparo_y

def disparo_seguro(amenaza, cuadrante): #Recibe amenaza y cuadrante
    am1 = amenaza.count('1') #Cantidad de amenazas grado 1
    am2 = amenaza.count('2') #Cantidad de amenazas grado 2
    disparo_x = '' #Pensadas y tecnicamente no usadas
    disparo_y = ''
    if cuadrante == "1": # Todos los enemigos estan en cuadrante 1
        if disparo_x == '':  #La termine usando aca, aunque tecnicamente se pueden eliminar 
            if '3' in amenaza: #Si hay amenaza grado 3 debe haber alguien al frente
                disparo_x = '-1'
            elif int(am1) >= int(am2): #Ve si hay mas amenazas de grado 1 que grado 2, si hay mas dispara en ese rango
                disparo_x = random.choice(["-4", "-5"])
            else: #dispara en el rango sobrante
                disparo_x = random.choice(["-2", "-3"])               
            disparo_y = '0'

            return disparo_x, disparo_y

    elif cuadrante == "2": # Todos los enemigos estan en cuadrante 2
        if disparo_x == '':  
            if '3' in amenaza:
                disparo_y = '-1'
            elif int(am1) >= int(am2): #Ve 
                disparo_y = random.choice(["-4", "-5"])
            else:
                disparo_y = random.choice(["-2", "-3"])               
            disparo_x = '0'

            return disparo_x, disparo_y
        
    elif cuadrante == "3": # Todos los enemigos estan en cuadrante 3
        if disparo_x == '': 
            if '3' in amenaza:
                disparo_x = '1'
            elif int(am1) >= int(am2): #Ve 
                disparo_x = random.choice(["4", "5"])
            else:
                disparo_x = random.choice(["2", "3"])               
            disparo_y = '0'

            return disparo_x, disparo_y        

    else: #Todos los enemigos estan en cuadrante 4
        if disparo_x == '':  #La termine usando aca, aunque tecnicamente se pueden eliminar 
            if '3' in amenaza:
                disparo_y = '1'
            elif int(am1) >= int(am2): #Ve 
                disparo_y = random.choice(["4", "5"])
            else:
                disparo_y = random.choice(["2", "3"])               
            disparo_x = '0'

            return disparo_x, disparo_y

def disparar(amenaza, cuadrante):
    c1 = int(cuadrante[0])
    c2 = int(cuadrante[1])
    c3 = int(cuadrante[2])
    c4 = int(cuadrante[3])
    am1 = amenaza.count('1')
    am2 = amenaza.count('2')
    if '3' in amenaza:
        if c1 >= c2 and c1 >= c3 and c1 >= c4:
            disparo_x = '-1'
            disparo_y = '0'
        elif c2 >= c1 and c2 >= c3 and c2 >= c4:
            disparo_x = '0'
            disparo_y = '-1'
        elif c3 >= c1 and c3 >= c2 and c3 >= c4:
            disparo_x = '1'
            disparo_y = '0'
        else:
            disapro_x = '0'
            disparo_y = '1'
        return disparo_x,disparo_y
    
    elif am2 > am1:
        if c1 >= c2 and c1 >= c3 and c1 >= c4:
            disparo_x = random.choice(['-2','-3'])
            disparo_y = '0'
        elif c2 >= c1 and c2 >= c3 and c2 >= c4:
            disparo_x = '0'
            disparo_y = random.choice(['-2','-3'])
        elif c3 >= c1 and c3 >= c2 and c3 >= c4:
            disparo_x = random.choice(['2','3'])
            disparo_y = '0'
        else:
            disapro_x = '0'
            disparo_y = random.choice(['-2','-3'])
        return disparo_x,disparo_y
    else:
        if c1 >= c2 and c1 >= c3 and c1 >= c4:
            disparo_x = random.choice(['-4','-5'])
            disparo_y = '0'
        elif c2 >= c1 and c2 >= c3 and c2 >= c4:
            disparo_x = '0'
            disparo_y = random.choice(['-4','-5'])
        elif c3 >= c1 and c3 >= c2 and c3 >= c4:
            disparo_x = random.choice(['4','5'])
            disparo_y = '0'
        else:
            disapro_x = '0'
            disparo_y = random.choice(['4','5'])
        return disparo_x,disparo_y

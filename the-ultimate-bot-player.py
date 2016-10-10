# coding=iso-8859-1 
import numpy
import random

def escoger_movimiento( amenazas ):
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
        if cuadrantes[3]< cuadrantes[0]:
            movimiento_y='1'
    elif minc ==cuadrantes[1]:
        movimiento_x='-1'
    elif minc==cuadrantes[2]:
        movimiento_y='-1'
    elif minc==cuadrantes[3]:
        movimiento_x='1'
    
    
    return movimiento_x + "," + movimiento_y

def escoger_disparo( amenazas ):
    ambos = amenazas.strip().split(':') #:V
    amenaza = ambos[0].strip().split('-') #Lista de amenzas [g1, g2, g3, gn]
    cuadrante = ambos[1].strip().split('-') #Lista de cuadrantes [c1, c2, c3, c4]    
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
    
    if len(amenaza) == 1:  #Cambio en el orden, si no hay amenazas no es necesario ver todo lo siguiente
        disparo_x, disparo_y = "0", "1" # R.I.P
    
    elif c1 != "0" and (c2 == c3 == c4 == "0"):
        disparo_x, disparo_y = disparo_seguro(amenaza, "1")
    elif c2 != "0" and (c1 == c3 == c4 == "0"):
        disparo_x, disparo_y = disparo_seguro(amenaza, "2")
    elif c3 != "0" and (c1 == c2 == c4 == "0"):
        disparo_x, disparo_y = disparo_seguro(amenaza, "3")
    elif c4 != "0" and (c1 == c2 == c2 == "0"):
        disparo_x, disparo_y = disparo_seguro(amenaza, "4")     
    elif (c1 != "0") and (c2 != "0") and (c3 != "0") and (c4 != "0"):
        disparo_x,disparo_y = disparar(amenaza,cuadrante) 
        
    return disparo_x + "," + disparo_y

def disparo_seguro(amenaza, cuadrante): # Recibe el cuadrante y la lista de amenzas ordenadas, hecho para no poner todo esto en la funcion escoger_disparo
    #am1 = amenaza.count('1')
    #am2 = amenaza.count('2')   Idea de respaldo en caso de que no funcione lo otro por index error.
    #am3 = amenaza.count('3')
    c = 0 #No existia la variable
    if cuadrante == "1": # Todos los enemigos estan en cuadrante 1
        while c < (len(amenaza)-1): #No se si esto evite el problema de index, o pongo por si acaso
            if amenaza[c] == amenaza[c+1]:#Esto va a tirar index error, hay que cambiar el [c+1]
                disparo_y = "0"
                if amenaza[c] == "1":
                    disparo_x = random.choice(["-4", "-5"])
                    break
                elif amenaza[c] == "2":
                    disparo_x = random.choice(["-2", "-3"])
                    break
            elif amenaza[c] == "3":
                disparo_x = "-1"
                disparo_y = '0'
                break    
            else:
                c += 1  
            #if disparo_x == '':              ##Parte de la idea de respaldo##
                #if int(am1) >= int(am2) and int(am1)>=int(am3):
                    #disparo_x = random.choice(["4", "5"])
            #elif int(am2)>=int(am1) and int(am2)>=int(am3):
                #disparo_x = random.choice(["2", "3"])
            #else:
                #disparo_x = '1'
                #disparo_y = '0'
                
    elif cuadrante == "2": # Todos los enemigos estan en cuadrante 2
        while c < (len(amenaza)-1):
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
                disparo_x = '0'
                break                 
            else:
                c +=1  
                
    elif cuadrante == "3": # Todos los enemigos estan en cuadrante 3
        while c < (len(amenaza)-1):
            if amenaza[c] == amenaza[c+1]:
                disparo_y = "0"
                if amenaza[c] == "1":
                    disparo_x = random.choice(["4", "5"])
                    break
                elif amenaza[c] == "2":
                    disparo_x = random.choice(["3", "2"])
                    break
            elif amenaza[c] == "3":
                disparo_x = "1"
                disparo_y = '0'
                break
            else:
                c += 1
    else: #Todos los enemigos estan en cuadrante 4
        while c < (len(amenaza)-1):
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
                disparo_x = '0'
                break                    
            else:
                c += 1
                
    return disparo_x, disparo_y

def disparar(amenaza, cuadrante):
    c1 = int(cuadrante[0])
    c2 = int(cuadrante[1])
    c3 = int(cuadrante[2])
    c4 = int(cuadrante[3])
    am1 = amenazas.count('1')
    am2 = amenazas.count('2')
    if '3' in amenaza:
        if c1 > c2 and c1>c3 and c1>c4:
            disparo_x = '-1'
            disparo_y = '0'
        elif c2 > c1 and c2 > c3 and c2 > c4:
            disparo_x = '0'
            disparo_y = '-1'
        elif c3>c1 and c3>c2 and c3>c4:
            disparo_x = '1'
            disparo_y = '0'
        else:
            disapro_x = '0'
            disparo_y = '1'
        return disparo_x,disparo_y
    elif am2 > am1:
        if c1 > c2 and c1>c3 and c1>c4:
            disparo_x = random.choice(['-2','-3'])
            disparo_y = '0'
        elif c2 > c1 and c2 > c3 and c2 > c4:
            disparo_x = '0'
            disparo_y = random.choice(['-2','-3'])
        elif c3>c1 and c3>c2 and c3>c4:
            disparo_x = random.choice(['2','3'])
            disparo_y = '0'
        else:
            disapro_x = '0'
            disparo_y = random.choice(['-2','-3'])
        return disparo_x,disparo_y
    else:
        if c1 > c2 and c1>c3 and c1>c4:
            disparo_x = random.choice(['-4','-5'])
            disparo_y = '0'
        elif c2 > c1 and c2 > c3 and c2 > c4:
            disparo_x = '0'
            disparo_y = random.choice(['-4','-5'])
        elif c3>c1 and c3>c2 and c3>c4:
            disparo_x = random.choice(['4','5'])
            disparo_y = '0'
        else:
            disapro_x = '0'
            disparo_y = random.choice(['4','5'])
        return disparo_x,disparo_y
    
##def disparar(amenaza, cuadrante): ##Deje comentado esto, la verdad no estoy seguro de como funcionaba, por eso lo deje asi##
##    cuenta = 0
##    amenaza_1 = 0
##    amenaza_2 = 0
##    while cuenta <= len(amenaza):
##        if   amenaza[cuenta] == '1':
##            amenaza_1 += 1
##            cuenta += 1
##        elif amenaza[cuenta] == '2':
##            amenaza_2 += 1
##            cuenta += 1
##        
##    if 3 in amenaza:
##        if cuadrante == 1:
##            disparo_x = "1"
##            disparo_y = "0"
##            return disparo_x, disparo_y
##        elif cuadrante == 2:
##            disparo_x = "0"
##            disparo_y = "-1"
##            return disparo_x, disparo_y
##        elif cuadrante == 3:
##            disparo_x = "-1"
##            disparo_y = "0"
##            return disparo_x, disparo_y
##        else:
##            disparo_x = "0"
##            disparo_y = "1"
##            return disparo_x, disparo_y
##    elif amenaza_2 >= amenaza_1:
##        if   cuadrante == 1:
##            disparo_x = random.choice(["3", "2"])
##            disparo_y = "0"
##            return disparo_x, disparo_y
##        elif cuadrante == 2:
##            disparo_x = "0"
##            disparo_y = random.choice(["-2", "-3"])
##            return disparo_x, disparo_y
##        elif cuadrante == 3:
##            disparo_x = random.choice(["-2", "-3"])
##            disparo_y = "0"
##            return disparo_x, disparo_y
##        else:
##            disparo_x = "0"
##            disparo_y = random.choice(["2", "3"])
##            return disparo_x, disparo_y
##    else:
##        if   cuadrante == 1:
##            disparo_x = random.choice(["5", "4"])
##            disparo_y = "0"
##            return disparo_x, disparo_y
##        elif cuadrante == 2:
##            disparo_x = "0"
##            disparo_y = random.choice(["-5", "-4"])
##            return disparo_x, disparo_y
##        elif cuadrante == 3:
##            disparo_x = random.choice(["-5", "-4"])
##            disparo_y = "0"
##            return disparo_x, disparo_y
##        else:
##            disparo_x = "0"
##            disparo_y = random.choice(["5", "4"])
##            return disparo_x, disparo_y



            

            
        
         

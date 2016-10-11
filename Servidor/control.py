#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Escrito por GasparCorrea
# gasparcorreavergara@gmail.com

"""
    Funciones utilizadas    

    validar_movimiento
    Chequea que el movimiento realizado por el jugador esta dentro de los valores esperados

    validar_disparo
    Análogo a validar_movimiento

    limites
    Permite el movimiento entre los limites del mapa. (Ej: Salir por arriba y entrar por abajo)

    evaluar_movimiento
    Entrega el resultado del movimiento:
        - True, en caso de que se realizo sin inconvenientes.
        - False, en caso de que hubo choque.
    
    evaluar_disparo
    Entrega el resultado del disparo:
        - True, en caso de haber golpeado a alguien.
        - Falso, disparo al agua.
    
    amenaza
    En base a una distancia, entrega el grado de amenaza

    estimar_amenazas
    En base a una posicion, entrega todas las amenazas respecto a esa posicion
    
    calcular_cuadrantes
    En base a una posicion, entrega la cantidad de enemigos en cada cuadrante relativo a la posicion

    spawn
    Asigna a un jugador una posicion inicial en el tablero


"""
import random

def validar_movimiento( movimiento ):
    posibles_movimientos = {(1,0),(-1,0),(0,1),(0,-1),(2,0),(-2,0),(0,2),(0,-2),(3,0),(-3,0),(0,3),(0,-3)}
    movimiento = movimiento[0], movimiento[1]
    return movimiento in posibles_movimientos

def validar_disparo( disparo ):
    posibles_disparos = {( -5 ,0),( -4 ,0),( -3 ,0),( -2 ,0),( -1 ,0),( 1 ,0),( 2 ,0),( 3 ,0),( 4 ,0),( 5 ,0),(0, -5 ),(0, -4 ),(0, -3 ),(0, -2 ),(0, -1 ),(0, 1 ),(0, 2 ),(0, 3 ),(0, 4 ),(0, 5 )}
    disparo =  disparo[0], disparo[1]
    return disparo in posibles_disparos


def limites( coordenada , limite):
    coordenada = [coordenada[0], coordenada[1]]
    for i in range(0,2):
        if (coordenada[i] >= limite):
            coordenada[i] = coordenada[i] - limite
        if ( coordenada[i] < 0):
            coordenada[i] = limite + coordenada[i]
    return coordenada

def evaluar_disparo(  battlefield, coordenada ):
    x, y = coordenada[0], coordenada[1]
    if ( battlefield[x][y] != 0 ):
        return True
    else: 
        return False

def evaluar_movimiento(battlefield, coordenada):
    x, y = coordenada[0], coordenada[1]
    if (battlefield[x][y] == 0):
        return True
    else:
        return False

def periodico ( r ,SIZE):
    if ( r >= SIZE ): return (SIZE-r)
    return r

def amenaza ( valor ):
    l = [3,2,2,1,1]
    return l [ abs ( valor ) -1 ]

def estimar_amenaza(posicion, battlefield, SIZE):
    amenazas = list()
    for i in xrange(2): # eje x e y
        for j in [-5,-4,-3,-2,-1,1,2,3,4,5]: # distancias visibles
            if (i == 0):
                if (battlefield[(posicion[0]+j)%SIZE][posicion[1]] != 0 ):
                    amenazas.append("-" + str(amenaza(j)))
            else:
                if (battlefield[posicion[0]][(posicion[1]+j)%SIZE] != 0 ):
                    amenazas.append("-" + str(amenaza(j)))
    random.shuffle(amenazas) # revolvemos amenazas para que no sea inferible/hackeable el juego
    return 'a'+ ''.join(amenazas)+":"+calcular_cuadrantes(battlefield, posicion, SIZE)

def spawn( battlefield , SIZE):
    while (1):
        x , y = random.randint(0,SIZE-1), random.randint(0,SIZE-1)
        if ( battlefield[x][y] == 0 ):
            return x,y

def calcular_cuadrantes(battlefield, posicion, SIZE):
    l = [0,0,0,0]
    x , y = posicion[0], posicion[1]
    for i in xrange(SIZE):
        for j in xrange(SIZE):
            if battlefield[i][j] !=0:
                if i <= x and j < y:
                    l[1] = l[1]+1
                elif i > x and j <= y:
                    l[0] = l[0]+1
                elif i < x and j >= y:
                    l[2] = l[2]+1
                elif i >= x and j > y:
                    l[3] = l[3]+1
                    
    l = map(str, l)
    return l[2]+"-"+l[1]+"-"+l[0]+"-"+l[3]

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Escrito por GasparCorrea
# gasparcorreavergara@gmail.com

import socket
import numpy
from control import *
import random 
import time


"""
    Aqui deben asignar valores para configurar la partida a su gusto
    IP: Escoger una ip distinta a localhost si es que desean jugar con otro computador
    PORT: No recomiendo cambiarlo, pero aun esta a su disposición cambiarlo
    NJ: Cantidad de bots que participaran en la partida
"""
IP = "localhost" 
PORT = 8888 
NJ = 3

if (NJ <= 5):
    SIZE = 11
elif (NJ <= 10):
    SIZE = 15
else:
    SIZE = 20

"""
    Funciones utilizadas:

   conectar
    Recibe todas las conexiones entrantes, y relaciona cada conexion con un nombre
    jugador

    spawn_all
    Situa a todos los jugadores en la matriz battlefield, y envia respectivas posiciones
    a cada jugadori

    matar
    Elimina la conexion con un jugador de la partida

    generar_id
    Asigna a cada usuario un id numérico, se usa para identificar al jugador internamente

"""

def matar( conexiones_entrantes, stats, id,jugador):
    del conexiones_entrantes[id]
    del stats[id]
    print "Se ha eliminado a ", jugador

def generar_id(conexiones_entrantes):
    while (1):
        id = random.randint(0,100)
        if not ( id in conexiones_entrantes) :
            return id

def conectar(server, log):
    log.append("juego:cargar")
    conexiones_entrantes = dict()
    while( len (conexiones_entrantes) < NJ ):
        socket_o, socket_info = server.accept()
        nombre_usuario = socket_o.recv(1024)
        id = generar_id( conexiones_entrantes )
        conexiones_entrantes[ id ] = (socket_o,socket_info,nombre_usuario)
        log.append("conectado:"+nombre_usuario)
        print "Conexion exitosa!"
    print "Todos se han conectado"
    return conexiones_entrantes


def spawn_all( battlefield , conexiones_entrantes, log):
    stats = dict()
    for id in conexiones_entrantes:
        socket_o = conexiones_entrantes[id][0]
        jugador = conexiones_entrantes[id][2]
        x, y = spawn( battlefield, SIZE)
        posicion = [x, y]
        stats[ id ] =[jugador,3,3,posicion]
        battlefield[x][y] = id
        log.append("aparecer:"+jugador+","+str(x)+","+str(y))
        print jugador," ha sido situado en "+str(x)+","+str(y)
        socket_o.send(str(x)+","+str(y))
    return stats

"""
    Estructuras utilizadas:
    conexiones entrantes es un diccionario cuyas llaves son el id del jugador, 
    y el valor es una tupla con un objeto socket,una tupla de ip, puerto, y el nombre del jugador.
    >>> conexiones_entrantes
    {'id':( socket_jugador, ( ip,puerto ),nombre_jugador)}

    stats es un diccionario cuyas llaves son el nombre del jugador, 
    y el valor es una tupla con las vidas, los turnos restantes, 
    y una tupla coordenadas.
    >>> stats
    {'id':(nombre_jugador,vidas, turnos restantes,(x,y))}

    battlefield es un np.array con valores 0 indicando espacios vacios, 
    y en los espacios en que estan situados los jugadores estan marcados 
    por sus respectivos id de jugador.
    >>> battlefield
    [[0,0,0],
     ['id_jugador_1',0,0],
     [0,id_jugador_2,0]]

"""
#Muy importante revisar el log una vez terminada la partida, el log entrega un resumen de lo que resulto la partida
log = list()
title = time.strftime("%c").replace(" ","_").replace(":","_").replace("/","-")
log.append("#TITLE;"+str(title)+"/"+str(SIZE))
title = title.replace(":","_").replace("/","-")
battlefield = numpy.tile(0,(SIZE,SIZE))
servidor = socket.socket( socket.AF_INET, socket.SOCK_STREAM)

# Si desea escoger un puerto en especifico cambiar 0, por PORT, de lo contrario, buscara cualquier puerto disponible
servidor.bind( (IP,0 ) ) 
# Indica a que IP y PORT deben conectarse los clientes
print servidor.getsockname()
servidor.listen(NJ)
print "Esperando Conexiones"
conexiones_entrantes = conectar(servidor, log)
log.append("juego:comenzar")
stats = spawn_all( battlefield, conexiones_entrantes, log)
print stats, "\n-------\n", conexiones_entrantes,"\n--------\n",battlefield
juego = 1

try:
    while ( juego ):
        if ( len(conexiones_entrantes) == 0):
            break 
        for id in conexiones_entrantes.keys():
            jugador = conexiones_entrantes[id][2]
            socket_o = conexiones_entrantes[id][0]
            #log.append("alertar:"+str(id))
            posicion = stats[id][3]
            x0, y0 = posicion[0], posicion[1]
            print "Alertando a ", jugador
            amenaza = estimar_amenaza(posicion, battlefield, SIZE)
            socket_o.send( amenaza )
            print "Esperando accion de ", jugador
            mensaje_recibido = socket_o.recv(1024)
            
            disparo = map(int,(mensaje_recibido.split("/")[0]).split(","))
            if not validar_disparo( disparo ):
                battlefield[x0][y0] = 0
                log.append("desconectar:{ID}".format(ID=jugador))
                matar(conexiones_entrantes,stats, id, jugador)
                print jugador," ha cometido disparo fuera de rango"

            movimiento = map(int,(mensaje_recibido.split("/")[1]).split(","))
            if not validar_movimiento( movimiento ):
                matar(conexiones_entrantes, stats, id , jugador)
                log.append("desconectar:{ID}".format(ID=jugador))
                battlefield[x0][y0] = 0
                print jugador," ha cometido un movimiento fuera de rango"

            disparo = posicion[0] + disparo[0], posicion[1] + disparo[1]
            posicion = posicion[0] + movimiento[0], posicion[1] + movimiento[1]
            print disparo, posicion
            disparo = limites( disparo, SIZE)
            posicion = limites( posicion, SIZE)
            
            estado = evaluar_disparo(battlefield, disparo)
            x, y = disparo[0], disparo[1]
            y = y if y >= 0 else SIZE + y
            x = x if x >= 0 else SIZE + x
            if ( estado ):
                id_golpeado = battlefield[x][y]
                stats[id_golpeado][1] = stats[id_golpeado][1] - 1
                stats[id][2] = stats[id][2] + 1
                stats[id][1] = stats[id][1] + 1
                jugador2 = stats[id_golpeado][0]
                log.append("disparar:{ID},{X},{Y},{ID2}".format(ID=jugador, X=x,Y=y,ID2=jugador2))
                log.append("muerte:{ID}".format(ID=jugador2))
                log.append("aparecer:"+jugador2+","+str(x)+","+str(y))
            else:
                stats[id][2] = stats[id][2] - 1
                log.append("disparar:{ID},{X},{Y},{OBJ}".format(ID=jugador, X=x,Y=y,OBJ="None"))            

            estado = evaluar_movimiento(battlefield, posicion)
            if ( estado ):
                x1, y1  = posicion[0], posicion[1]
                battlefield[x0][y0] = 0
                stats[id][3] = x1, y1
                battlefield[x1][y1] = id
                x1 = x1 if x1 >= 0 else SIZE + x1
                y1 = y1 if y1 >= 0 else SIZE + y1
                log.append("moverse:{ID},{X},{Y}".format(ID=jugador, X=x1,Y=y1))
            else:
                x1, y1  = posicion[0], posicion[1]
                id_golpeado = battlefield[x1][y1]
                print jugador, " ha chocado a ", stats[id_golpeado][0]," ", jugador," sera destruido"
                matar( conexiones_entrantes, stats, id,jugador)
                log.append("desconectar:{ID}".format(ID=jugador))
                battlefield[x0][y0] = 0
                stats[id_golpeado][1]-=1
                jugador2 = stats[id_golpeado][0]
                log.append("colision:{ID}".format(ID = jugador))
                log.append("colision:{ID}".format(ID = jugador2))
            for ids in stats.keys():
                if ( stats[ids][2] == 0 ):
                    stats[ids][1] = stats[ids][1]-1;
                    stats[ids][2] = 3;
                if ( stats[ids][1] == 0 ):
                    jugador_in_for = stats[ids][0]
                    x_ids, y_ids = stats[ids][3]
                    battlefield[x_ids][y_ids] = 0
                    log.append("desconectar:{ID}".format(ID=jugador_in_for))
                    matar( conexiones_entrantes, stats, ids ,jugador_in_for)        

except KeyboardInterrupt:
    print "STOP IT!"

except Exception as e:
    print "Unexpected error:", type(e), "Argumentos",e.args

servidor.close()
log.append("juego:terminar")
with open("../Visualizacion/logs/"+title+".log","w") as log_file:
    for linea in log:
        log_file.write(linea+"\n")



# Escrito por GasparCorrea
# gasparcorreavergara@gmail.com

import socket
from random import randint
from botdummy import *

def spawn(cliente):
    mensaje = cliente.recv(1024)
    posicion = mensaje.split(",")
    return int(posicion[0]), int(posicion[1])
cliente = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
IP = raw_input("ingrese la ip ")
if not IP:
    IP = '127.0.0.1'
PORT = input("ingrese el puerto ")
cliente.connect( (IP ,PORT ) )
print "Conectado"
name  = randint(0,991)
cliente.send( "dummy{0}".format(name) )
posicion = spawn(cliente) 

juego = 1
print "Start"
try:
    while (juego):

        mensaje = cliente.recv(1024)
        amenazas = mensaje.split(":")[0]
        disparo = escoger_disparo( amenazas )
        movimiento = escoger_movimiento()
        mensaje = disparo + "/" + movimiento
        cliente.send( mensaje )
except socket.error:
    cliente.close()
    print "GAME OVER"


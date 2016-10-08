import socket
from botplayer import *

def spawn(cliente):
    mensaje = cliente.recv(1024)
    posicion = mensaje.split(",")
    return int(posicion[0]), int(posicion[1])

#LOGIN
cliente = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
IP = raw_input("ingrese la ip ")
PORT = input("ingrese el puerto ")
cliente.connect( (IP ,PORT ) )
usuario = raw_input( "Ingrese nombre de usuario:" )
cliente.send( usuario )

#SPAWN INICIAL
posicion = spawn(cliente) 

juego = 1
try:
    while (juego):

        #Recibir mensaje del servidor
        mensaje = cliente.recv(1024)

        # mensaje, es el string de amenazas, en base a aquel mensaje, tomar una decision
        
        """
        escoger_disparo( mensaje ) se encuentra en botdummy, es tarea de ustedes completar esta funcion.

        escoger_movimieto( mensaje ) se encuentra en botdummy, es tarea de ustedes completar esta funcion.

        """
        disparo = escoger_disparo( mensaje )        
        movimiento = escoger_movimiento( mensaje )
        mensaje =  disparo+"/"+movimiento
        cliente.send(mensaje )
except socket.error:
    cliente.close()
    print "GAME OVER"

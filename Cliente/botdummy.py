# Escrito por GasparCorrea
# gasparcorreavergara@gmail.com


"""
Funciones utilizadas

    escoger
        En base a una accion(disparo o movimiento), escoge un numero aleatorio.
    
    escoger_movimiento
        Escoge movimiento aleatorio
    
    escoger_disparo
        Escoge disparo aleatorio en base a la amenaza.

"""


import numpy
import random



def escoger ( accion ):
    if ( accion == 3 ):
        l = [-1,1]
        return random.choice(list(l))
    elif( accion == 1 ):
        l = [-5,-4,4,5]
        return random.choice(list(l))
    elif( accion == 2 ):
        l = [-3,-2,2,3]
        return random.choice(list(l))


def escoger_movimiento ( ):
    
    delta = escoger(3)
    if ( random.randint(0,1) ):
        return "0,"+ str(delta)

    return str( delta ) +",0"

def escoger_disparo ( amenaza ):
    amenaza = amenaza.split("-")
    if (len( amenaza ) > 1 ):
        accion = int( amenaza[1] )
    else:
        accion = random.randint(1,3)

    delta = escoger( accion )
    
    if( random.randint(0,1) ):
        return str( delta )+",0" 
    
    return "0,"+ str( delta )


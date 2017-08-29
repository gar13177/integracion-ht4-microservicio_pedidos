from time import sleep

from autenticacion.servicios import *
from ordenes.servicios import *
from promociones.servicios import *

SLEEP_TIME = 1.5 #seconds

def atender_ordenes(cola):
    cola.agregar_orden({
        'usuario':{
            'email':'1@1',
            'contrasena':'contrasena',
            'token':''
        },
        'token':1
    })
    while True:
        print 'orden'
        orden = cola.tomar_orden()
        if orden == None:
            sleep(SLEEP_TIME)
        else:
            print 'dentro'
            usuario = Servicios_de_Autenticacion().iniciar_sesion(orden['usuario'])
            orden = Servicios_de_Ordenes().nueva_orden(usuario)
            
            



def atender_inicio_de_sesion(cola):
    while True:
        print 'sesion'
        inicio_de_sesion = cola.tomar_inicio_de_sesion()
        if inicio_de_sesion == None:
            sleep(SLEEP_TIME)

def atender_promociones(cola):
    while True:
        print 'promocion'
        promocion = cola.tomar_promocion()
        if promocion == None:
            sleep(SLEEP_TIME)

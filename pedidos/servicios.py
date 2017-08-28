from autenticacion.servicios import *
from ordenes.servicios import *
from promociones.servicios import *


auth = Servicios_de_Autenticacion()
usuario = auth.iniciar_sesion({
    'email':'1@1',
    'contrasena':'asdtsa',
    'token':'astasd'
})

print usuario

ordenes = Servicios_de_Ordenes()
orden = ordenes.nueva_orden(usuario)
orden.agregar_item({
    'nombre':'coca-cola',
    'cantidad':4,
    'id':''
})

orden.agregar_item({
    'nombre':'pan',
    'cantidad':3,
    'id':''
})
print orden
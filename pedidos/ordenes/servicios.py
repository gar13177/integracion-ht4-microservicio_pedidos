from modelos.orden import Orden

class Servicios_de_Ordenes(object):
    def __init__(self):
        pass

    def nueva_orden(self, usuario):
        orden = Orden(usuario)
        return orden

    def agregar_item_a_orden(self,orden,item):
        orden.agregar_item(item)
        return orden

    def pagar_orden(self, orden):
        orden.pagar()
        return orden

    def actualizar_estado(self, orden, estado):
        orden.nuevo_estado(estado)
        return orden


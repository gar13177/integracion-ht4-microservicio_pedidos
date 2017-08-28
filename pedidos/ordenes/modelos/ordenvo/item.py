from comunicacion.externo.consultas_erp import item_existe, obtener_item_de_erp

class Item(object):
    def __init__(self,nombre, cantidad, id=''):
        self.nombre = nombre
        self.cantidad = cantidad
        self.id = id

    def __str__(self):
        return str(self.nombre)+":"+str(self.cantidad)

    def es_valido(self):
        existe = item_existe(self)
        return existe

    def actualizar_de_erp(self):
        item = obtener_item_de_erp(self)
        self = item
        return item


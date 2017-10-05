from autenticacion.modelos.usuario import Usuario, UsuarioNoValido
from comunicacion.externo.consultas_erp import obtener_precio_de_item, finalizar_orden
from ordenvo.item import Item

class ErrorDeFacturacion(Exception):
    def __init__(self):#, errors):
        message = "problema al generar la factura"
        super(ErrorDeFacturacion, self).__init__(message)
        #self.errors = errors

class Orden(object):
    def __init__(self,usuario):
        if not isinstance(usuario, Usuario):
            usuario = Usuario(**usuario)
        self.usuario = usuario
        self.items = []
        self.esta_pagada = False
    
    def __str__(self):
        text = 'usuario: '+str(self.usuario) + ' orden: '
        for item in self.items:
            text+=str(item)+';'
        return text

    def agregar_item(self, item):
        item = Item(
            item['nombre'],
            item['cantidad'],
            item['id']
        )
        self.items.append(item)

    def pagar_orden(self):
        pago_total = 0
        for item in self.items:
            pago_total += obtener_precio_de_item(item)

        orden_valida = self.generar_orden_en_erp()
        if not orden_valida:
            raise ErrorDeFacturacion()

        self.esta_pagada = True
        return pago_total
    
    def generar_orden_en_erp(self):
        orden_valida = finalizar_orden(self)
        return orden_valida


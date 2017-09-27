import json
from modelos.orden import Orden
from autenticacion.servicios import Servicios_de_Autenticacion
from comunicacion.externo.consultas_erp import revisar_orden_en_erp
from rabbitmq.ProcessOrder import process_order as actualizar_estado_de_orden

class Servicios_de_Ordenes(object):
    def __init__(self):
        pass

    def consultar_orden_a_erp(self, orden):
        data_usuario = {"token":orden['token']}
        usuario = Servicios_de_Autenticacion().iniciar_sesion(data_usuario)

        mensaje_a_usuario = json.dumps({"message":"estamos atendiendo tu orden"}, ensure_ascii=False).encode('utf8')
        
        actualizar_estado_de_orden(usuario.token, mensaje_a_usuario)
        estado_de_orden = revisar_orden_en_erp(orden)
        estado_de_orden = json.dumps(estado_de_orden, ensure_ascii=False).encode('utf8')
        actualizar_estado_de_orden(usuario.token, estado_de_orden)
        print('consulta de orden terminada')

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

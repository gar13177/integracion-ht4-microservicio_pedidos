from comunicacion.basededatos.consultas import crear_promocion

class Servicios_de_Promocion(object):
    def __init__(self):
        pass

    def nueva_promocion(self, promocion):
        mi_promocion = dict()
        mi_promocion['descripcion'] = "descuento: %s, tipo: %s, descripcion: %s"%(
            promocion['descuento'],
            promocion['tipoPromocion']['tipo'],
            promocion['descripcionPromocion']['descripcion']
        )
        mi_promocion['fecha_expiracion'] = promocion['fechaFinalPromo']
        crear_promocion(mi_promocion)
        
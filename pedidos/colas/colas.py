class Colas(object):
    def __init__(self):
        self.ordenes = []
        self.autenticacion = []
        self.promociones = []

    def agregar_orden(self,orden):
        self.ordenes.append(orden)

    def agregar_inicio_de_sesion(self, inicio_de_sesion):
        self.autenticacion.append(inicio_de_sesion)

    def agregar_promocion(self, promocion):
        self.promociones.append(promocion)

    def tomar_orden(self):
        if len(self.ordenes) > 0:
            return self.ordenes.pop()
        return None

    def tomar_inicio_de_sesion(self):
        if len(self.autenticacion) > 0:
            return self.autenticacion.pop()
        return None

    def tomar_promocion(self):
        if len(self.promociones) > 0:
            return self.promociones.pop()
        return None
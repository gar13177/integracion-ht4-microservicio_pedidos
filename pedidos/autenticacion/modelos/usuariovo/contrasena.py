class ContrasenaMuyCorta(Exception):
    def __init__(self):#, errors):
        message = "contrasena muy corta"
        super(ContrasenaMuyCorta, self).__init__(message)
        #self.errors = errors

class Contrasena(object):
    def __init__(self,contrasena):
        if len(contrasena) <= 0:
            raise ContrasenaMuyCorta()
        
        self.contrasena = contrasena

    def __str__(self):
        return self.contrasena
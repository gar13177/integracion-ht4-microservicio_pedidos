from usuariovo.email import Email
from usuariovo.contrasena import Contrasena

from comunicacion.basededatos.consultas import usuario_con_sesion_iniciada
from comunicacion.externo.consultas_erp import usuario_en_erp, obtener_usuario_de_erp

class UsuarioNoExistente(Exception):
    def __init__(self):#, errors):
        message = "usuario no existe en el ERP"
        super(UsuarioNoExistente, self).__init__(message)
        #self.errors = errors

class UsuarioNoValido(Exception):
    def __init__(self):#, errors):
        message = "usuario no valido"
        super(UsuarioNoValido, self).__init__(message)
        #self.errors = errors

class Usuario(object):
    def __init__(self,
            email,
            contrasena,
            token
        ):
        if not (email == None or email == ''):
            self.email = Email(email)
        else:
            self.email = None

        if not (contrasena == None or contrasena == ''):
            self.contrasena = Contrasena(contrasena)
        else:
            self.contrasena = None
        
        if self.email == None and self.contrasena == None:
            if token == None or token == '':
                raise UsuarioNoValido()
            else:
                self.token = token
                self.actualizar_de_erp()

        self.token = None

    def __str__(self):
        return str(self.email)+" "+str(self.contrasena)+" "+str(self.token)

    def esta_registrado(self):
        sesion_iniciada = usuario_con_sesion_iniciada(self)        
        return sesion_iniciada

    def existe_en_erp(self):
        usuario_en_erp = usuario_en_erp(self)
        return usuario_en_erp        

    def actualizar_de_erp(self):
        usuario = obtener_usuario_de_erp(self)
        if usuario == None:
            raise UsuarioNoExistente()
        self = usuario
        return usuario
            
from usuariovo.email import Email
from usuariovo.contrasena import Contrasena

from comunicacion.basededatos.consultas import usuario_con_sesion_iniciada, obtener_usuario_de_db, crear_usuario
from comunicacion.externo.consultas_erp import usuario_en_erp, obtener_usuario_de_erp
from dateutil.parser import parse
import datetime, pytz

class FechaDeExpiracionNoValida(Exception):
    def __init__(self):#, errors):
        message = "fecha de expiracion no valida"
        super(FechaDeExpiracionNoValida, self).__init__(message)
        #self.errors = errors

class FechaExpirada(Exception):
    def __init__(self):#, errors):
        message = "fecha de sesion vencida"
        super(FechaExpirada, self).__init__(message)
        #self.errors = errors

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
            email=None,
            contrasena=None,
            token=None,
            fecha_expiracion=None
        ):
        self.actualizar_email(email)

        self.actualizar_contrasena(contrasena)

        if fecha_expiracion != None:
            self.actualizar_fecha_de_expiracion(fecha_expiracion)
        else:
            self.fecha_expiracion = None

        if not (token == None or token == ''):
            self.token = token
        else:
            if self.email == None and self.contrasena == None:
                raise UsuarioNoValido()
            self.token = None

    def __str__(self):
        return str(self.email)+" "+str(self.contrasena)+" "+str(self.token)

    def actualizar_fecha_de_expiracion(self, fecha):
        if fecha != None:
            fecha = parse(fecha)
            if fecha > self.fecha_actual():
                self.fecha_expiracion = fecha
                return 
            raise FechaExpirada()
        raise FechaDeExpiracionNoValida()

    def fecha_actual(self):
        fecha = datetime.datetime.utcnow()
        fecha = fecha.replace(tzinfo=pytz.utc)
        return fecha

    def es_valido(self):
        if self.token == None:
            if self.existe_en_erp():
                self.actualizar_de_erp()
                return True
        else:
            if self.esta_registrado():
                return True
        return False

    def actualizar_email(self, email):
        if not (email == None or email == ''):
            self.email = Email(email)
        else:
            self.email = None

    def actualizar_contrasena(self, contrasena):
        if not (contrasena == None or contrasena == ''):
            self.contrasena = Contrasena(contrasena)
        else:
            self.contrasena = None

    def esta_registrado(self):
        sesion_iniciada = usuario_con_sesion_iniciada(self)        
        return sesion_iniciada

    def existe_en_erp(self):
        existe = usuario_en_erp(self)
        return existe   

    def actualizar_de_copia_local(self):
        usuario = obtener_usuario_de_db(self)
        if usuario == None:
            raise UsuarioNoExistente()
        self = usuario
        return usuario   

    def actualizar_de_erp(self):
        usuario = obtener_usuario_de_erp(self)
        if usuario == None:
            raise UsuarioNoExistente()
        self = usuario
        return usuario

    def guardar_copia_local(self):
        valido = crear_usuario(self)
        return valido

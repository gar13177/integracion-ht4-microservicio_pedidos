from modelos.usuario import Usuario, UsuarioNoExistente

class Servicios_de_Autenticacion(object):
    def __init__(self):
        pass

    def iniciar_sesion(self, usuario):
        usuario = Usuario(
            usuario['email'],
            usuario['contrasena'],
            usuario['token']
        )
        
        if usuario.esta_registrado():
            return usuario
    
        if usuario.existe_en_erp():
            usuario = usuario.actualizar_de_erp()
            return usuario

        raise UsuarioNoExistente()

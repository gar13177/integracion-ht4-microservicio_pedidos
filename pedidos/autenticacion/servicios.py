from modelos.usuario import Usuario, UsuarioNoExistente

class Servicios_de_Autenticacion(object):
    def __init__(self):
        pass

    def iniciar_sesion(self, usuario):
        """
        email=None,
        contrasena=None,
        token=None,
        fecha_expiracion=None
        """
        usuario = Usuario(**usuario)
        
        if usuario.esta_registrado():
            usuario = usuario.actualizar_de_copia_local()
            return usuario
    
        if usuario.existe_en_erp():
            usuario = usuario.actualizar_de_erp()
            usuario.guardar_copia_local()
            return usuario

        raise UsuarioNoExistente()

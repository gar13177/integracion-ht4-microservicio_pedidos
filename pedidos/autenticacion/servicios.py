from modelos.usuario import Usuario, UsuarioNoExistente

class Servicios_de_Autenticacion(object):
    def __init__(self):
        pass

    def iniciar_sesion(self, usuario):
        usuario = Usuario(
            usuario['email'],
            usuario['contrasena'],
            ''# token
        )
        
        if usuario.esta_registrado():
            usuario = usuario.actualizar_de_copia_local()
            return usuario
    
        if True:#usuario.existe_en_erp():
            #usuario = usuario.actualizar_de_erp()
            usuario.guardar_copia_local()
            return usuario

        raise UsuarioNoExistente()

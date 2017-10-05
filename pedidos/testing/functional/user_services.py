import unittest, datetime, pytz

class TestUserServices(unittest.TestCase):
    def test_newuser(self):
        from autenticacion.modelos.usuario import Usuario
        
        fecha = datetime.datetime.utcnow() + datetime.timedelta(days=1) 
        fecha = fecha.replace(tzinfo=pytz.utc)
        constants = {
            "email":"prueba@prueba",
            "contrasena": "prueba",
            "fecha_expiracion": str(fecha)
        }
        usuario = Usuario(**constants)
        self.assertEqual("prueba@prueba prueba None", str(usuario))

    def test_newuserwithtoken(self):
        from autenticacion.modelos.usuario import Usuario
        
        fecha = datetime.datetime.utcnow() + datetime.timedelta(days=1) 
        fecha = fecha.replace(tzinfo=pytz.utc)
        constants = {
            "token":"abc",
            "fecha_expiracion": str(fecha)
        }
        usuario = Usuario(**constants)
        self.assertEqual("None None abc", str(usuario))

    def test_updateexpirationdate(self):

        from autenticacion.modelos.usuario import Usuario, FechaExpirada
        
        usuario = Usuario(token="abc")

        fecha = datetime.datetime.utcnow() + datetime.timedelta(days=-1) 
        fecha = fecha.replace(tzinfo=pytz.utc)
        
        self.assertRaises(FechaExpirada, usuario.actualizar_fecha_de_expiracion,fecha=str(fecha))

    def test_updateexpirationdate2(self):
        from autenticacion.modelos.usuario import Usuario, FechaDeExpiracionNoValida
        usuario = Usuario(token="abc")
        self.assertRaises(FechaDeExpiracionNoValida, usuario.actualizar_fecha_de_expiracion,fecha=None)


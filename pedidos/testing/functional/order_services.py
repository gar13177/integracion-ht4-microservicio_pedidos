import unittest, datetime, pytz

class TestOrderServices(unittest.TestCase):
    def test_neworder(self):
        from autenticacion.modelos.usuario import Usuario
        from ordenes.modelos.orden import Orden
        
        fecha = datetime.datetime.utcnow() + datetime.timedelta(days=1) 
        fecha = fecha.replace(tzinfo=pytz.utc)
        constants = {
            "email":"prueba@prueba",
            "contrasena": "prueba",
            "fecha_expiracion": str(fecha)
        }
        usuario = Usuario(**constants)
        orden = Orden(usuario)
        self.assertEqual("usuario: prueba@prueba prueba None orden: ", str(orden))
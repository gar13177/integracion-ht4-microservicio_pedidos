from servicios import *
import json, pprint
# 1 es inicio de sesion
# 2 es nueva orden
# 3 es nueva promocion

def cola(sdata):
    data_cruda = json.loads(sdata)
    tipo_transaccion = data_cruda['tipo']
    data_real = data_cruda['data']

    
    if tipo_transaccion == 1:
        # es inicio de sesion
        respuesta = 'inicio de sesion'
        data_usuario = {}
        data_usuario['email'] = data_real['user']
        data_usuario['contrasena'] = data_real['password']

        try:
            usuario = Servicios_de_Autenticacion().iniciar_sesion(data_usuario)
            respuesta = {
                'message': 'welcome %s, your token is %s'%(usuario.email.user,usuario.token),
                'token': usuario.token
            }
            respuesta = json.dumps(respuesta, ensure_ascii=False).encode('utf8')
        except Exception as e:
            respuesta = e.message
            print e.message

    elif tipo_transaccion == 2:
        # es nueva orden
        respuesta = 'nueva orden'
    elif tipo_transaccion == 3:
        # es promocion
        respuesta = 'promociones'
    else:
        respuesta = "Error en solicitud"

    return respuesta
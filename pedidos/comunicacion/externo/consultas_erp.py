from rabbitmq.LoginValidationERP import LoginValidationErp
from rabbitmq.OrderValidationERP import OrderValidationERP
from uuid import uuid4
import json

def usuario_en_erp(usuario):
    usuario_data = {
        "user_name": str(usuario.email),
        "password": usuario.contrasena
    }
    usuario_data = json.dumps(usuario_data, ensure_ascii=False).encode('utf8')
    erp_connection = LoginValidationErp()
    print("check user on login: "+str(usuario_data))
    response = erp_connection.call(usuario_data)
    response = json.loads(response)
    if 'err' in response:
        return False
    #print("got: "+str(response))
    return True


def obtener_usuario_de_erp(usuario):
    usuario_data = {
        "user_name": str(usuario.email),
        "password": usuario.contrasena
    }
    usuario_data = json.dumps(usuario_data, ensure_ascii=False).encode('utf8')
    erp_connection = LoginValidationErp()
    print("get user on login: "+str(usuario_data))
    response = erp_connection.call(usuario_data)
    response = json.loads(response)
    if 'err' in response:
        return None

    usuario.token = response['token']
    usuario.actualizar_fecha_de_expiracion(response['date_expiration'])
    return usuario

def revisar_orden_en_erp(orden):
    # ordern = {{}} = dict()
    orden = json.dumps(orden, ensure_ascii=False).encode('utf8')
    erp_connection = OrderValidationERP()
    print("check order: "+str(orden))
    return {"message":"la orden fue validada"}


def item_existe(args):
    return True

def obtener_item_de_erp(args):
    return None

def obtener_precio_de_item(args):
    return 0.0

def finalizar_orden(args):
    return True
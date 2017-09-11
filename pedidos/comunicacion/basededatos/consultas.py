import requests
import uuid

BASE_PATH = 'http://localhost:8003/'
USER_PATH = 'usuario'

def usuario_con_sesion_iniciada(usuario):
    if usuario.token != None:
        payload = {'id_usuario':usuario.token}
    else:
        payload = {'nombre':str(usuario.email),'contrasena':usuario.contrasena}
    r = requests.get(BASE_PATH+USER_PATH, params=payload)
    if r.status_code == requests.codes.ok:
        
        return True
    print str(r)
    return False

def obtener_usuario_de_db(usuario):
    if usuario.token != None:
        payload = {'id_usuario':usuario.token}
    else:
        payload = {'nombre':str(usuario.email),'contrasena':usuario.contrasena}
    r = requests.get(BASE_PATH+USER_PATH, params=payload)
    if r.status_code == requests.codes.ok:
        data = r.json()[0] # se obtiene el primer registro
        print (data)
        usuario.actualizar_fecha_de_expiracion(data['fecha_expiracion'])
        usuario.token = data['id_usuario']
        usuario.actualizar_email(data['nombre'])
        usuario.actualizar_contrasena(data['contrasena'])
        return usuario
    print (r)
    return None

def crear_usuario(usuario):
    payload = {
        'id_usuario': usuario.token,
        'fecha_expiracion': '2017-09-27T00:00',
        'nombre': str(usuario.email),
        'contrasena': str(usuario.contrasena)
    }
    r = requests.post(BASE_PATH+USER_PATH+'/', data=payload)
    if r.status_code == requests.codes.ok:
        data = r.json()
        print data
        return True
    print str(r)
    print str(r.text)
    return False

import requests
import uuid

def usuario_con_sesion_iniciada(usuario):
    payload = {'nombre':usuario.email.user}
    r = requests.get('http://localhost:8003/usuario', params=payload)
    if r.status_code == requests.codes.ok:
        return True
    return False

def obtener_usuario_de_db(usuario):
    payload = {'nombre':usuario.email.user}
    r = requests.get('http://localhost:8003/usuario', params=payload)
    if r.status_code == requests.codes.ok:
        data = r.json()
        usuario.token = data[0]['id_usuario']
        return usuario
    return None

def crear_usuario(usuario):
    usuario.token = str(uuid.uuid4())
    payload = {
        'id_usuario': usuario.token,
        'fecha_expiracion': '2017-08-27T00:00',
        'nombre': usuario.email.user,
        'contrasena': 'c'
    }

    r = requests.post('http://localhost:8003/usuario/', data=payload)
    if r.status_code == requests.codes.ok:
        data = r.json()
        print data
        return True
    else:
        print 'error'
        print r
    return False

def obtener_token_de_sesion():
    pass
import pika, json
from autenticacion.servicios import *

LOGIN_FROM_CLIENT_QUEUE = 'login_from_client_queue'

def on_request(ch, method, props, body):
    usuario = json.loads(body)
    print usuario

    data_usuario = {}
    data_usuario['email'] = usuario['user']
    data_usuario['contrasena'] = usuario['password']

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

    response = respuesta

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

def new_login():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=LOGIN_FROM_CLIENT_QUEUE)
    
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(on_request, queue=LOGIN_FROM_CLIENT_QUEUE)
    print("recepcion de logins iniciada")
    channel.start_consuming()
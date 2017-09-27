import pika, json
from constants import HOST
from promociones.servicios import Servicios_de_Promocion

def callback(ch, method, properties, body):
    promocion = json.loads(body)
    Servicios_de_Promocion().nueva_promocion(promocion)
    print promocion


def new_promotion():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
    channel = connection.channel()

    channel.queue_declare(queue='new_promotion')
    channel.basic_consume(callback,
                      queue='new_promotion',
                      no_ack=True)
    print("recepcion de promociones")

    channel.start_consuming()
import pika, json
from constants import HOST

def callback(ch, method, properties, body):
    promocion = json.loads(body)
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
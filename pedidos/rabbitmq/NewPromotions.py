import pika, json, thread
from constants import HOST, PROMOTION_QUEUE, MAX_PROMOTION_THREADS
from promociones.servicios import Servicios_de_Promocion

def new_thread():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
    channel = connection.channel()

    channel.queue_declare(queue=PROMOTION_QUEUE)
    channel.basic_consume(callback,
                      queue=PROMOTION_QUEUE,
                      no_ack=True)
    channel.start_consuming()

def callback(ch, method, properties, body):
    promocion = json.loads(body)
    Servicios_de_Promocion().nueva_promocion(promocion)
    print promocion

def new_promotion():
    print("recepcion de promociones")
    for i in range(MAX_PROMOTION_THREADS):
        try:
            thread.start_new_thread(new_thread, ())
        except Exception as e:
            print("new thread promotion error: "+str(e.message))

    
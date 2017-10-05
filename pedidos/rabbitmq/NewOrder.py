import pika, json, thread
from constants import HOST, ORDER_QUEUE, MAX_ORDER_THREADS
from ordenes.servicios import Servicios_de_Ordenes
from ProcessOrder import process_order

def new_thread():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
    channel = connection.channel()

    channel.queue_declare(queue=ORDER_QUEUE)
    channel.basic_consume(callback,
                      queue=ORDER_QUEUE,
                      no_ack=True)
    channel.start_consuming()

def callback(ch, method, properties, body):
    orden = json.loads(body)
    try:
        Servicios_de_Ordenes().consultar_orden_a_erp(orden)
    except Exception as e:
        token = orden['token']
        respuesta = json.dumps({"message":e.message}, ensure_ascii=False).encode('utf8')
        process_order(token, respuesta)

def new_order():
    print("recepcion de ordenes")
    for i in range(MAX_ORDER_THREADS):
        try:
            thread.start_new_thread(new_thread, ())
        except Exception as e:
            print("new thread order error: "+str(e.message))
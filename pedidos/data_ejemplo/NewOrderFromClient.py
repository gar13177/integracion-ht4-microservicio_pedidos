#!/usr/bin/env python
import pika, json

HOST = 'localhost'
ORDER_QUEUE = 'los_del_call'
ORDER_UPDATES = 'order_updates'

def recieve_callback(ch, method, properties, body):
    print("Actualizacion recibida: "+str(body))

def recieve_order(token):
    print('token para cola: '+str(token))
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
    channel = connection.channel()

    channel.exchange_declare(exchange=ORDER_UPDATES)
                            #,type='direct')

    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange=ORDER_UPDATES,
                    queue=queue_name,
                    routing_key=token)

    channel.basic_consume(recieve_callback,
                        queue=queue_name,
                        no_ack=True)

    channel.start_consuming()


def new_order(token):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
    channel = connection.channel()

    order['token'] = token
    message = json.dumps(order)

    channel.queue_declare(queue=ORDER_QUEUE)

    channel.basic_publish(exchange='',
                        routing_key=ORDER_QUEUE,
                        body=message)
    print("Nueva orden solicitada "+str(message))
    connection.close()

order = {
	"token":"a8a43c1a-6caa-41c9-a5d5-4284f7f84ea7",
	"order":
		{
			"address": "A101",
			"status": "RECEIVED",
			"products": [
				{
					"product": "Cocacola",
					"qty": 1
				},
				{
					"product": "Hamburguesa",
					"qty": 1
				}
			]
		}	
}
#!/usr/bin/env python
import pika, json, unittest

HOST = 'localhost'
ORDER_QUEUE = 'los_del_call'
ORDER_UPDATES = 'order_updates'

connection = None
response = None

def recieve_callback(ch, method, properties, body):

    global connection, response
    response = json.loads(body)
    connection.close()


def recieve_order(token):
    global connection
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
    connection.close()

order = {
	"token":"1",
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

class TestNewOrder(unittest.TestCase):
    def test_neworder(self):
        token = u'1'
        new_order(token)
        recieve_order(token)
        global response
        self.assertTrue("message" in response)
        self.assertEqual(response["message"], u"estamos atendiendo tu orden")
        
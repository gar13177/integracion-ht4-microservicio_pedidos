#!/usr/bin/env python
import pika
import sys
from constants import HOST, ORDER_UPDATES

def process_order(token, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
    channel = connection.channel()

    channel.exchange_declare(exchange=ORDER_UPDATES)
                            #,type='direct')

    channel.basic_publish(exchange=ORDER_UPDATES,
                        routing_key=token,
                        body=message)
    print("Orden Procesada. User: %s, Mensaje: %s" % (token, message))
    connection.close()
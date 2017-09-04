import pika, json



def callback(ch, method, properties, body):
    promocion = json.loads(body)
    print promocion


def get_promotions():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='new_promotion')
    channel.basic_consume(callback,
                      queue='new_promotion',
                      no_ack=True)

    channel.start_consuming()
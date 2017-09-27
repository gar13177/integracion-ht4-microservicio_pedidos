import pika, json
HOST = 'localhost'
def new_promotion():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
    channel = connection.channel()

    message = json.dumps(promocion)

    channel.queue_declare(queue='new_promotion')

    channel.basic_publish(exchange='',
                        routing_key='new_promotion',
                        body=message)
    print("Nueva promocion solicitada "+str(message))
    connection.close()

promocion = {
    "descuento": 0,
    "tipoPromocion": {
        "tipo": "2x1"
    },
    "descripcionPromocion": {
        "descripcion": "Martes y Jueves "
    },
    "fechaInicioPromo": "2017-08-07T00:00:00.000Z",
    "fechaFinalPromo": "2017-08-20T00:00:00.000Z",
    "color": "azul",
    "_id": "59b70ab30cbe323e8cd16677"
}

new_promotion()
import pika, uuid, json, thread, pprint, unittest

LOGIN_FROM_CLIENT_QUEUE = 'login_from_client_queue'
HOST = 'localhost'

class LoginRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, data):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key=LOGIN_FROM_CLIENT_QUEUE ,
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=data)
        while self.response is None:
            self.connection.process_data_events()
        return self.response



class TestLogin(unittest.TestCase):
    def test_login(self):
        login_rpc = LoginRpcClient()
        inicio_de_sesion = {
            "user":"prueba@prueba",
            "password": "prueba"
        }

        response = login_rpc.call(json.dumps(inicio_de_sesion))
        response = json.loads(response)
        token = response['token']
        self.assertEqual(u'1',token)

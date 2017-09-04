#from autenticacion.modelos.usuario import Usuario

def usuario_en_erp(args):
    fibonacci_rpc = FibonacciRpcClient()

    print(" [x] Requesting fib(30)")
    response = fibonacci_rpc.call(30)
    print(" [.] Got %r" % response)
    return True


def obtener_usuario_de_erp(args):
    fibonacci_rpc = FibonacciRpcClient()
    response = fibonacci_rpc.call(30)
    print(" [.] Got %r" % response)
    return {}

def item_existe(args):
    return True

def obtener_item_de_erp(args):
    return None

def obtener_precio_de_item(args):
    return 0.0

def finalizar_orden(args):
    return True
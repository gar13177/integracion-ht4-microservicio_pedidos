import thread

from colas.colas import Colas
from servicios import atender_inicio_de_sesion, atender_ordenes, atender_promociones

from rabbitmq.PromotionServer import get_promotions


if __name__ == "__main__":
    #colas = Colas()
    #fibonacci_rpc = FibonacciRpcClient()

    #print(" [x] Requesting fib(30)")
    #response = fibonacci_rpc.call(30)
    #print(" [.] Got %r" % response)
    try:
        #thread.start_new_thread(atender_inicio_de_sesion, (colas,))
        thread.start_new_thread(get_promotions)
        #thread.start_new_thread(atender_promociones, (colas,))
    except:
        print "Error: unable to start thread"

    while 1:
        pass

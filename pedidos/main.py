import thread

from colas.colas import Colas
#from servicios import atender_inicio_de_sesion, atender_ordenes, atender_promociones

from rabbitmq.PromotionServer import get_promotions
from rabbitmq.LoginRpcServer import new_login

if __name__ == "__main__":
    try:
        thread.start_new_thread(get_promotions, ())
        thread.start_new_thread(new_login, ())
    except Exception as e:
        print e.message
        print "Error: unable to start thread"

    while 1:
        pass

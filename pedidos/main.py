import thread

from colas.colas import Colas
from servicios import atender_inicio_de_sesion, atender_ordenes, atender_promociones

if __name__ == "__main__":
    colas = Colas()

    try:
        #thread.start_new_thread(atender_inicio_de_sesion, (colas,))
        thread.start_new_thread(atender_ordenes, (colas,))
        #thread.start_new_thread(atender_promociones, (colas,))
    except:
        print "Error: unable to start thread"

    while 1:
        pass

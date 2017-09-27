import thread, time 
from rabbitmq.NewPromotions import new_promotion
from rabbitmq.LoginFromUser import new_login
from rabbitmq.NewOrder import new_order

if __name__ == "__main__":
    try:
        thread.start_new_thread(new_promotion, ())
        thread.start_new_thread(new_login, ())
        thread.start_new_thread(new_order, ())
    except Exception as e:
        print e.message
        print "Error: unable to start thread"

    var = True
    while var:
        try:
            time.sleep(60)
        except KeyboardInterrupt:
            var = False
        except Exception as e:
            print e.message

#prueba para jenkins
# prueba para jenkins2 
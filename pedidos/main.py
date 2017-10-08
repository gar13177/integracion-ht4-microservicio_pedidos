import thread, time 
from rabbitmq.NewPromotions import new_promotion
from rabbitmq.LoginFromUser import new_login
from rabbitmq.NewOrder import new_order

def run_main(var):
    try:
        thread.start_new_thread(new_promotion, ())
        new_login()
        #thread.start_new_thread(new_login, ())
        thread.start_new_thread(new_order, ())
    except Exception as e:
        print e.message
        print "Error: unable to start thread"

    while var:
        try:
            time.sleep(60)
        except KeyboardInterrupt:
            var = False
        except Exception as e:
            print e.message

if __name__ == "__main__":
    run_main(True)
    

#prueba para jenkins

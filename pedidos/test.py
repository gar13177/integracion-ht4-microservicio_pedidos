import threading, time, sys, os, multiprocessing

from testing.functional.user_services import *
from testing.functional.order_services import *
from testing.integration.login_test import TestLogin
from testing.integration.order_test import TestNewOrder
from testing.stress.stress_test import stress_test
from main import run_main

def run_main_process(cond):
    sys.stdout = open(os.devnull, "w")
    run_main(cond)
    sys.stdout = sys.__stdout__

if __name__ == "__main__":
    cond = True
    try:
        t1 = multiprocessing.Process(target=run_main_process, args=(cond,))
        t1.start()
    except Exception as e:
        print e.message
        print "Error: unable to start process"

    print "tests ready"
    unittest.main(exit=False)
    stress_test()
    cond = False
    try:
        t1.terminate()
    except Exception as e:
        print e.message
        print "Error: unable to stop process"
    
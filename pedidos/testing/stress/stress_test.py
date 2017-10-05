from stress_test_login import stress_test as stress_test_login
from stress_test_order import stress_test as stress_test_order

def stress_test():
    stress_test_login()
    stress_test_order()
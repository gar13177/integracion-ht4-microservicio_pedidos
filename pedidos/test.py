from testing.functional.user_services import *
from testing.functional.order_services import *
from testing.integration.login_test import TestLogin
from testing.integration.order_test import TestNewOrder
from testing.stress.stress_test import stress_test

print "tests ready"

#unittest.main()

stress_test()
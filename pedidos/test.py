from testing.functional.user_services import *
from testing.functional.order_services import *
from testing.integration.login_test import TestLogin
from testing.integration.order_test import TestNewOrder
import testing.integration.test_cp
import testing.stress.test_db

print "tests ready"

unittest.main()
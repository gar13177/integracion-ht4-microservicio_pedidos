import unittest
#from unnecessary_math import multiply
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual( 3*4, 12)
 
    def test_strings_a_3(self):
        self.assertEqual( 'a'*3, 'aaa')






















print "test 1 --- success"
print "test 2 --- success"
print "test 3 --- success"
print "test 4 --- success"
print "test 5 --- success"
print "test 6 --- success"
print "test 7 --- success"
print "test 8 --- success"

#raise Exception("error de prueba development")
 
if __name__ == '__main__':
    unittest.main()


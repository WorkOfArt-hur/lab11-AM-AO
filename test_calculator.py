import unittest
from calculator import *
# https://github.com/WorkofArt-hur/lab11-AM-AO
# Partner 1: Arthur Mozzoni
# Partner 2: Alejandro Ortiz
class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3,0),3)
        self.assertEqual(add(101.1, 50.2), 151.3)
        self.assertEqual(add(-5,8), 3)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(3,0), 3)
        self.assertEqual(subtract(101.5, 60.5), 51.0)
        self.assertEqual(subtract(-100, 20), -120)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(3,2),6)
        self.assertEqual(multiply(5,6),30)
        self.assertEqual(multiply(-9,9),81)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(4,2),2)
        self.assertEqual(divide(27,9),3)
        self.assertEqual(divide(36,6),6)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
             divide(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(9,3),2)
        self.assertEqual(logarithm(10000, 10), 4)
        self.assertNotEqual(logarithm(4,0),0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-1,4)
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(3, -2)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(5,12),13)
        self.assertEqual(hypotenuse(-3,-4),5)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertEqual(ValueError):
            square_root(-4)
            
        self.assertEqual(square_root(16),4)
        self.assertEqual(square_root(36),6)
        self.assertEqual(square_root(81),9)
    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
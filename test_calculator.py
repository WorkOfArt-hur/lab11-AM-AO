import unittest
from calculator import *
# https://github.com/WorkofArt-hur/lab11-AM-AO
# Partner 1: Arthur Mozzoni
# Partner 2: Alejandro Ortiz
class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(sum(3,0),3)
        self.assertEqual(sum(101.1, 50.2), 151.3)
        self.assertEqual(sum(-5,8), 3)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(3,0), 3)
        self.assertEqual(sub(101.5, 60.5), 51.0)
        self.assertEqual(sub(-100, 20), -120)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
             div(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(9,3),2)
        self.assertEqual(log(10000, 10), 4)
        self.assertNotEqual(log(4,0),0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(-1,4)
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
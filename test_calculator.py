import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    # def test_add(self):
    #     assert 0 + 3
    #     assert

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(3,2), 6)
        self.assertEqual(multiply(5,4), 20)
        self.assertEqual(multiply(-12,5), -60)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(2,2), 1)
        self.assertEqual(divide(32,4), 8)
        self.assertEqual(divide(49,7), 7)
    ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(-1,4)
    ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(5,12), 13)
        self.assertEqual(hypotenuse(-3,-4), 5)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        with self.assertRaises(ValueError):
            square_root(-16)
        # Test basic function
        self.assertEqual(square_root(36), 6)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(81), 9)
    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
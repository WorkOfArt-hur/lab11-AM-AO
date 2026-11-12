# https://github.com/WorkofArt-hur/lab11-AM-AO
# Partner 1: Arthur Mozzoni
# Partner 2: Alejandro Ortiz
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3,0),3)
        self.assertEqual(add(101.1, 50.2), 151.3)
        self.assertEqual(add(-5,8), 3)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(3, 0), 3)
        self.assertEqual(subtract(101.5, 60.5), 41.0)  
        self.assertEqual(subtract(-100, -20), -80)     

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 2), 6)
        self.assertEqual(mul(-9, 9), -81)              
        self.assertEqual(mul(-4, -5), 20)              

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 4), 2)
        self.assertEqual(div(9, -27), -3)              
        self.assertEqual(div(2, 5), 2.5)               
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
             div(0, 5)                                 

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(3,9),2)
        self.assertEqual(logarithm(10, 10000), 4)
        self.assertEqual(logarithm(2, 4),2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-1,4)
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(3, -2)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(5,12),13)
        self.assertEqual(hypotenuse(-3,-4),5)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
            
        self.assertEqual(square_root(16),4)
        self.assertEqual(square_root(36),6)
    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()

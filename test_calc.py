#import unittest package
import unittest
import calc

#All the unittest class should derived from unittest.TestCase
#This is the only way to execute the test functions inside the class
class TestCalc(unittest.TestCase):
    #setUp function will call before each and every test case run/ setUp function will call at starting
    def setUp(self):
        self.a = 20
        self.b = 10

    #method name start with keyword test, because the mechanism behind running the class will give the status of those test cases by considering the methods which uses test keyword
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(self.a, self.b), 30)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)
        self.assertEqual(calc.subtract(self.a, self.b), 10)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
        self.assertEqual(calc.multiply(self.a, self.b), 200)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)
        self.assertEqual(calc.divide(self.a, self.b), 2)

    #tearDown method is the one which will execute at last after running all those test cases
    #def tearDown():
        #clear data

# To run the unittest we need to invoke main function of unit test framework
if __name__ == '__main__':
    unittest.main()
import unittest
import calc


# we are inheriting the test from the parameter within
class TestCalc(unittest.TestCase):
    # method should start with the test
    def test_add(self):
        result = calc.add(10, 5)
        result2 = calc.add(-1,1)
        self.assertEqual(result, 15)
        self.assertEqual(result2, 0)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)

    def test_divide(self):
        self.assertEqual(calc.divide(5,2), 2.5)
        # now we will test the




if __name__ == '__main__':
    unittest.main()

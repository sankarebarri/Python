import unittest
from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):

    def test_area(self):
        # Test  for radius >= 0
        self.assertAlmostEqual(circle_area(2), pi*(2**2))
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)

    def test_values(self):
        # Make sure the radius is not negative
        self.assertRaises(ValueError, circle_area, -2)
        self.assertRaises(ValueError, circle_area, -7)

    def test_types(self):
        # Make sure the radius is a non negative integer or float
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, 'radius')
        self.assertRaises(TypeError, circle_area, True)
#print(circle_area(1))
import unittest
from app import addition

class TestAddition(unittest.TestCase):
    def testaddition(self):
        self.assertEqual(addition(2, 3),5)
        self.assertEqual(addition(-1, 1),0)
        self.assertEqual(addition(0, 0),0)

from app import soustraction

class TestSoustraction(unittest.TestCase):
    def testaddition(self):
        self.assertEqual(soustraction(2, 3),-1)
        self.assertEqual(soustraction(-1, 1),-2)
        self.assertEqual(soustraction(0, 0),0)

if name == '__main':
    unittest.main()

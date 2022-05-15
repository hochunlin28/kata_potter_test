import unittest
from discount import Discount_counter

class DiscountTest(unittest.TestCase):
    def setUp(self):
        self.ctr = Discount_counter()

    def test_Basics(self):
        self.assertEqual(0, self.ctr.price([]))
        
    def test_Basics1(self):
        self.assertEqual(8, self.ctr.price([1]))

    def test_Basics2(self):    
        self.assertEqual(8, self.ctr.price([2]))

    def test_Basics3(self):    
        self.assertEqual(8, self.ctr.price([3]))

    def test_Basics4(self):
        self.assertEqual(8, self.ctr.price([4]))
        
    def test_Basics5(self):
        self.assertEqual(8 * 3, self.ctr.price([1, 1, 1]))


if __name__ == '__main__':
    unittest.main()
import unittest
import gcd


class TestGcd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_gcd_basic(self):
        self.assertEqual(gcd.gcd(54, 888), 6)
        self.assertEqual(gcd.gcd(5, 10), 5)
        self.assertEqual(gcd.gcd(888, 54), 6)
        self.assertEqual(gcd.gcd(10, 5), 5)

    def test_gcd_low(self):
        self.assertEqual(gcd.gcd(7, 17), 1)
        self.assertEqual(gcd.gcd(1, 2), 1)

    def test_gcd_zero(self):
        self.assertEqual(gcd.gcd(0, 5), 5)
        self.assertEqual(gcd.gcd(5, 0), 5)

    def test_gcd_same(self):
        self.assertEqual(gcd.gcd(7, 7), 7)
        self.assertEqual(gcd.gcd(0, 0), 0)

    def test_gcd_negative(self):
        self.assertEqual(gcd.gcd(-5, 10), 5)
        self.assertEqual(gcd.gcd(5, -10), 5)
        self.assertEqual(gcd.gcd(-5, -10), 5)


if __name__ == '__main__':
    unittest.main()

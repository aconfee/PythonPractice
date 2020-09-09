import unittest
import negateBinary


class TestConvertToBinary(unittest.TestCase):

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

    def test_negate_binary(self):
        result = negateBinary.negateBinary(['0', '1', '1', '0', '0'])
        expected = ['1', '0', '1', '0', '0']
        for resultElement, expectedElement in zip(result, expected):
            self.assertEqual(resultElement, expectedElement)

    def test_negate_binary_fast(self):
        result = negateBinary.negateBinaryFast(['0', '1', '1', '0', '0'])
        expected = ['1', '0', '1', '0', '0']
        for resultElement, expectedElement in zip(result, expected):
            self.assertEqual(resultElement, expectedElement)


if __name__ == '__main__':
    unittest.main()

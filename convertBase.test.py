import unittest
import convertBase


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

    def test_convert_binary(self):
        result = convertBase.convertToBase(50, 2)
        expected = [1, 1, 0, 0, 1, 0]
        for resultElement, expectedElement in zip(result, expected):
            self.assertEqual(resultElement, expectedElement)

    def test_convert_base10(self):
        result = convertBase.convertToBase(50, 10)
        expected = [5, 0]
        for resultElement, expectedElement in zip(result, expected):
            self.assertEqual(resultElement, expectedElement)

    def test_convert_base3(self):
        # 1, 3, 9, 27
        # 2, 1, 2, 1
        # 2 = two of these. For the number twenty, the two means two tens. Here, we have one twenty-seven, two nines, etc.
        result = convertBase.convertToBase(50, 3)
        expected = [1, 2, 1, 2]
        for resultElement, expectedElement in zip(result, expected):
            self.assertEqual(resultElement, expectedElement)


if __name__ == '__main__':
    unittest.main()

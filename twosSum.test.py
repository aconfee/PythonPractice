import unittest
import twosSum


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

    def test_two_pointer_method(self):
        result = twosSum.twoSumTwoPointer([1, 2, 3, 4, 6], 7)
        expected = [[0, 4], [2, 3]]
        for resultElement, expectedElement in zip(result, expected):
            self.assertEqual(resultElement[0], expectedElement[0])
            self.assertEqual(resultElement[1], expectedElement[1])

    def test_hash_method(self):
        result = twosSum.twoSumHash([1, 2, 3, 4, 6], 7)
        expected = [[0, 4], [2, 3]]
        for resultElement, expectedElement in zip(result, expected):
            self.assertEqual(resultElement[0], expectedElement[0])
            self.assertEqual(resultElement[1], expectedElement[1])


if __name__ == '__main__':
    unittest.main()

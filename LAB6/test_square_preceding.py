import unittest
from square_preceding import square_preceding


class TestSquare(unittest.TestCase):
    def test_square_preceding(self):
        test_list = [1,2,3]
        self.assertEqual(square_preceding(test_list), [0,1,4])

if __name__ == "__main__":
    unittest.main()

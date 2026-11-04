import unittest
from app.main import simple_interest


class TestSimpleInterest(unittest.TestCase):

    def test_normal_calculation(self):
        self.assertEqual(simple_interest(10000, 7, 2), 1400.0)

    def test_zero_interest(self):
        self.assertEqual(simple_interest(10000, 0, 2), 0.0)


if __name__ == "__main__":
    unittest.main()

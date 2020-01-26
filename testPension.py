import unittest
from datetime import date
from pension import pension

class TestPension(unittest.TestCase):

    def test_male_valid_worker(self):
        self.assertTrue(pension())


    def test_male_invalid_worker(self):
        self.assertFalse(pension())


    def test_female_valid_worker(self):
        self.assertTrue(pension())


    def test_female_invalid_worker(self):
        self.assertFalse(pension())


    def test_male_unhealthy_valid_worker(self):
        self.assertTrue(pension())


    def test_male_unhealthy_invalid_worker(self):
        self.assertFalse(pension())


    def test_female_unhealthy_valid_worker(self):
        self.assertTrue(pension())

    def test_female_unhealthy_invalid_worker(self):
        self.assertFalse(pension())


if __name__ == '__main__':
    unittest.main()

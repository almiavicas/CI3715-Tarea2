import unittest
import math
from datetime import date
from pension import pension

# Helper constants
WEEKS_PER_YEAR = 52
NEEDED_WEEKS = 750
SUFFICIENT_YEARS = date.today().year - math.ceil(NEEDED_WEEKS / WEEKS_PER_YEAR)
INSUFFICIENT_YEARS = date.today().year - math.floor(NEEDED_WEEKS / WEEKS_PER_YEAR)


class TestPension(unittest.TestCase):


    def test_male_valid_worker(self):
        year = SUFFICIENT_YEARS
        month = date.today().month
        day = date.today().day
        workDate = date(year, month, day)
        birthDate = date(date.today().year - 61, month, day)
        self.assertTrue(pension(workDate, birthDate, False, False))


    def test_male_invalid_worker(self):
        year = INSUFFICIENT_YEARS
        month = date.today().month
        day = date.today().day
        workDate = date(year, month, day)
        birthDate = date(date.today().year - 59, month, day)
        self.assertFalse(pension(workDate, birthDate, False, False))


    def test_female_valid_worker(self):
        year = SUFFICIENT_YEARS
        month = date.today().month
        day = date.today().day
        workDate = date(year, month, day)
        birthDate = date(date.today().year - 56, month, day)
        self.assertTrue(pension(workDate, birthDate, False, True))


    def test_female_invalid_worker(self):
        year = INSUFFICIENT_YEARS
        month = date.today().month
        day = date.today().day
        workDate = date(year, (month - 1 % 12) + 1, (day + 2 % 28) + 1)
        birthDate = date(date.today().year - 45, month, day)
        self.assertFalse(pension(workDate, birthDate, False, True))


    def test_male_unhealthy_valid_worker(self):
        year = SUFFICIENT_YEARS - 20
        month = date.today().month
        day = date.today().day
        workDate = date(year, month, day)
        birthDate = date(date.today().year - 56, (month + 3 % 12) + 1, (day + 3 % 28) + 1)
        self.assertTrue(pension(workDate, birthDate, True, False))


    def test_male_unhealthy_invalid_worker(self):
        year = INSUFFICIENT_YEARS
        month = date.today().month
        day = date.today().day
        workDate = date(year, month, day)
        birthDate = date(date.today().year - 54, month, day)
        self.assertFalse(pension(workDate, birthDate, True, False))


    def test_female_unhealthy_valid_worker(self):
        year = SUFFICIENT_YEARS - 20
        month = date.today().month
        day = date.today().day
        workDate = date(year, month, day)
        birthDate = date(date.today().year - 51, month, day)
        self.assertTrue(pension(workDate, birthDate, True, True))


    def test_female_unhealthy_invalid_worker(self):
        year = INSUFFICIENT_YEARS
        month = date.today().month
        day = date.today().day
        workDate = date(year, month, day)
        birthDate = date(date.today().year - 49, month, day)
        self.assertFalse(pension(workDate, birthDate, True, True))

if __name__ == '__main__':
    unittest.main()

import unittest
import math
from datetime import date
from pension import pension

WEEKS_PER_YEAR = 52
# Semanas necesarias para obtener la pension
NEEDED_WEEKS = 750

class TestPension(unittest.TestCase):

    def test_male_valid_worker(self):
        year = date.today().year - math.ceil(NEEDED_WEEKS / WEEKS_PER_YEAR)
        month = date.today().month
        day = date.today().day
        workDate = date(year, month, day)
        birthDate = date(date.today().year - 61, month, day)
        self.assertTrue(pension(workDate, birthDate, False, False))


    def test_male_invalid_worker(self):
        year = date.today().year - math.floor(NEEDED_WEEKS / WEEKS_PER_YEAR)
        month = date.today().month
        day = date.today().day
        workDate = date(year, month, day)
        birthDate = date(date.today().year - 62, month, day)
        self.assertFalse(pension(workDate, birthDate, False, False))


    # def test_female_valid_worker(self):
    #     year = date.today().year - 58
    #     month = date.today().month
    #     day = date.today().day
    #     workDate = date(year, month, day)
    #     birthDate = date(year - 18, month, day)
    #     self.assertTrue(pension(workDate, birthDate, False, True))


    # def test_female_invalid_worker(self):
    #     year = date.today().year - 55
    #     month = date.today().month
    #     day = date.today().day
    #     workDate = date(year, month - 1 % 12, day + 2 % 28)
    #     birthDate = date(year - 28, month, day)
    #     self.assertFalse(pension(workDate, birthDate, False, True))


    # def test_male_unhealthy_valid_worker(self):
    #     year = 1964
    #     month = 3
    #     day = 14
    #     workDate = date(year, month, day)
    #     birthDate = date(year - 22, month + 3, day + 3)
    #     self.assertTrue(pension(workDate, birthDate, True, False))


    # def test_male_unhealthy_invalid_worker(self):
    #     self.assertFalse(pension())


    # def test_female_unhealthy_valid_worker(self):
    #     self.assertTrue(pension())


    # def test_female_unhealthy_invalid_worker(self):
    #     self.assertFalse(pension())


if __name__ == '__main__':
    unittest.main()

import unittest
from datetime import date
from pension import pension

class TestPension(unittest.TestCase):

    def test_male_valid_worker(self):
        year = date.today().year - 70
        month = date.today().month
        day = date.today().day
        workDate = date(year, month, day)
        birthDate = date(year - 20, month, day)
        self.assertTrue(pension(workDate, birthDate, False, False))


    def test_male_invalid_worker(self):
        year = date.today().year - 50
        month = date.today().month
        day = date.today().day
        workDate = date(year, month, day)
        birthDate = date(year - 20, month, day)
        self.assertFalse(pension(workDate, birthDate, False, False))


    def test_female_valid_worker(self):
        year = date.today().year - 58
        month = date.today().month
        day = date.today().day
        workDate = date(year, month, day)
        birthDate = date(year - 18, month, day)
        self.assertTrue(pension(workDate, birthDate, False, True))


    # def test_female_invalid_worker(self):
    #     year = date.today().year - 70
    #     month = date.today().month
    #     day = date.today().day
    #     workDate = date(year, month, day)
    #     birthDate = date(year - 20, month, day)
    #     self.assertFalse(
    #         pension(
    #             date(date.today().year - 55, date.today().month - 1, date.today().day + 3),
    #             date(date.today().year - 90, date.today().month, date.today().day),
    #             False,
    #             True
    #         )
    #     )


    # def test_male_unhealthy_valid_worker(self):
    #     self.assertTrue(pension())


    # def test_male_unhealthy_invalid_worker(self):
    #     self.assertFalse(pension())


    # def test_female_unhealthy_valid_worker(self):
    #     self.assertTrue(pension())


    # def test_female_unhealthy_invalid_worker(self):
    #     self.assertFalse(pension())


if __name__ == '__main__':
    unittest.main()

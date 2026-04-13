import unittest
from age import categorize_by_age

class TestCategorizeByAge(unittest.TestCase):
    def test_adolescent_age(self):
        for number in range(10,19):
            with self.subTest(number=number):
                self.assertEqual(categorize_by_age(number), "Adolescent")
                print(f"\n{number} is consider as an adolescent")
                
    def test_adult_age(self):
        for number in range(30,40):
            with self.subTest(number=number):
                    self.assertEqual(categorize_by_age(number), "Adult")
                    print(f"\n{number} is consider as an adult")


    def test_golden_age(self):
        for number in range(70,80):
            with self.subTest(number=number):
                    self.assertEqual(categorize_by_age(number), "Golden age")
                    print(f"\n{number} is consider as a golden age")

if __name__ == "__main__":
    unittest.main(verbosity=2)
import unittest
from app.bmi_calculator import calculate_bmi, get_bmi_category

class TestBMICalculator(unittest.TestCase):

    def test_bmi_underweight(self):
        # BMI < 18.5, should return "Underweight"
        bmi = calculate_bmi(100, 5, 5)  # 100 lbs, 5 feet 5 inches
        category = get_bmi_category(bmi)
        self.assertEqual(category, "Underweight")

    def test_bmi_normal(self):
        # 18.5 <= BMI < 24.9, should return "Normal weight"
        bmi = calculate_bmi(150, 5, 5)  # 150 lbs, 5 feet 5 inches
        category = get_bmi_category(bmi)
        self.assertEqual(category, "Normal weight")

    def test_bmi_overweight(self):
        # 25 <= BMI < 29.9, should return "Overweight"
        bmi = calculate_bmi(200, 5, 5)  # 200 lbs, 5 feet 5 inches
        category = get_bmi_category(bmi)
        self.assertEqual(category, "Overweight")

    def test_bmi_obese(self):
        # BMI >= 30, should return "Obese"
        bmi = calculate_bmi(250, 5, 5)  # 250 lbs, 5 feet 5 inches
        category = get_bmi_category(bmi)
        self.assertEqual(category, "Obese")

    def test_bmi_invalid_input(self):
        # Testing for invalid input
        with self.assertRaises(ValueError):
            calculate_bmi("invalid", 5, 5)

if __name__ == '__main__':
    unittest.main()

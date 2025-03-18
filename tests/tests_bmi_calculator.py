import unittest
from app.bmi_calculator import calculate_bmi, get_bmi_category

class TestBMICalculator(unittest.TestCase):

    def test_bmi_underweight(self):
        bmi = calculate_bmi(100, 5, 5)  # 100 lbs, 5 feet 5 inches
        category = get_bmi_category(bmi)
        self.assertEqual(category, "Underweight")

    def test_bmi_normal(self):
        bmi = calculate_bmi(145, 5, 5)  # 150 lbs, 5 feet 5 inches
        category = get_bmi_category(bmi)
        self.assertEqual(category, "Normal weight")

    def test_bmi_overweight(self):
        bmi = calculate_bmi(175, 5, 5)  # 200 lbs, 5 feet 5 inches
        category = get_bmi_category(bmi)
        self.assertEqual(category, "Overweight")

    def test_bmi_obese(self):
        bmi = calculate_bmi(250, 5, 5)  # 250 lbs, 5 feet 5 inches
        category = get_bmi_category(bmi)
        self.assertEqual(category, "Obese")

    def test_bmi_invalid_input_weight(self):
        # Testing for invalid input
        with self.assertRaises(ValueError):
            calculate_bmi("invalid", 5, 5)

    def test_bmi_invalid_input_height_feet(self):
        # Testing for invalid input
        with self.assertRaises(ValueError):
            calculate_bmi(150, "invalid", 5)
    
    def test_bmi_invalid_input_height_inches(self):
        # Testing for invalid input
        with self.assertRaises(ValueError):
            calculate_bmi(150, 5, "invalid")

if __name__ == '__main__':
    unittest.main()

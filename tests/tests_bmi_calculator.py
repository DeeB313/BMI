import unittest
from app.bmi_calculator import calculate_bmi, get_bmi_category

class TestBMICalculator(unittest.TestCase):

    def test_bmi_underweight(self):
        bmi = calculate_bmi(100, 5, 5)  # 100 lbs, 5 feet 5 inches
        category = get_bmi_category(bmi)
        self.assertEqual(category, "Underweight")
        print(f"Test 1: BMI = {bmi:.2f},  Expected Category: {category}")

    def test_bmi_normal_lower_bound(self):
        bmi = calculate_bmi(109, 5, 5)  # 150 lbs, 5 feet 5 inches
        category = get_bmi_category(bmi)
        self.assertEqual(category, "Normal weight")
        print(f"Test 2: BMI = {bmi:.2f},  Expected Category: {category}")

    def test_bmi_normal_upper_bound(self):
        bmi = calculate_bmi(146.7, 5, 5)  # 150 lbs, 5 feet 5 inches
        category = get_bmi_category(bmi)
        self.assertEqual(category, "Normal weight")
        print(f"Test 3: BMI = {bmi:.2f},  Expected Category: {category}")


    def test_bmi_overweight_lower_bound(self):
        bmi = calculate_bmi(146.8, 5, 5)  # 200 lbs, 5 feet 5 inches
        category = get_bmi_category(bmi)
        self.assertEqual(category, "Overweight")
        print(f"Test 4: BMI = {bmi:.2f},  Expected Category: {category}")
    
    def test_bmi_overweight_upper_bound(self):
        bmi = calculate_bmi(176, 5, 5)  # 200 lbs, 5 feet 5 inches
        category = get_bmi_category(bmi)
        self.assertEqual(category, "Overweight")
        print(f"Test 5: BMI = {bmi:.2f},  Expected Category: {category}")

    def test_bmi_obese(self):
        bmi = calculate_bmi(200, 5, 5)  # 250 lbs, 5 feet 5 inches
        category = get_bmi_category(bmi)
        self.assertEqual(category, "Obese")
        print(f"Test 6: BMI = {bmi:.2f},  Expected Category: {category}")

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

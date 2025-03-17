def get_bmi_category(bmi):
    """Classifies BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def calculate_bmi(weight_pounds, height_feet, height_inches):
    """Calculates BMI given weight in pounds and height in feet and inches."""
    
    # Check if the inputs are valid
    if not isinstance(weight_pounds, (int, float)) or not isinstance(height_feet, int) or not isinstance(height_inches, int):
        raise ValueError("Invalid input: Weight and height must be numbers.")
    
    # Convert height from feet and inches to meters
    height_meters = ((height_feet * 12) + height_inches) * 0.0254
    
    # Convert weight from pounds to kilograms
    weight_kg = weight_pounds * 0.453592
    
    # BMI formula
    bmi = weight_kg / (height_meters ** 2)
    
    return bmi

def get_bmi_category(bmi):
    """Classifies BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate_bmi(weight_pounds, height_feet, height_inches):
    """Calculates BMI given weight in pounds and height in feet and inches."""


    if not isinstance(weight_pounds,(int, float)):
        raise ValueError("Weight must be a number.")
    
    if not isinstance(height_feet,(int, float)):
        raise ValueError("Height (feet) must be a number.")
    
    if not isinstance(height_inches,(int, float)):
        raise ValueError("Height (inches) must be a number.")
    
    # Convert height from feet and inches to meters
    height_inches = (height_feet * 12) + height_inches
    height_meters = height_inches * 0.025
    
    # Convert weight from pounds to kilograms
    weight_kg = weight_pounds * 0.45
    
    # BMI formula
    bmi = weight_kg / (height_meters ** 2)
    
    # Debugging output
    print(f"Weight: {weight_kg} kg, Height: {height_meters} meters, BMI: {bmi}")
    
    return bmi


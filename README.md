BMI Calculator
This is a simple BMI Calculator project that calculates and classifies the Body Mass Index (BMI) based on user input (height in feet and inches, and weight in pounds). The application calculates BMI using the formula:

BMI = (weight in kilograms) / ( height in meters )^2

​
 
Based on the calculated BMI, the application classifies the individual into one of the following categories:

Underweight: BMI < 18.5

Normal weight: 18.5 ≤ BMI < 25

Overweight: 25 ≤ BMI < 30

Obese: BMI ≥ 30





REQUIREMENTS
To run this BMI Calculator application, you need the following:

 - Python 3.x (for the backend calculation)
 - unittest module (for running the tests)
 - Git (optional, for version control)


Installation
1. Clone the Repository
  #git clone https://github.com/DeeB313/BMI.git
  #cd BMI

2. Set Up a Virtual Environment (Optional but recommended)

  #python -m venv venv


    -> Activate the virtual environment (Windows):
      #.\venv\Scripts\activate


    -> Activate the virtual environment (MacOS):
      #source venv/bin/activate


3. Install Dependencies (if needed)
If you are using any additional dependencies (like unittest or other libraries), make sure they are installed within the virtual environment:
  #pip install -r requirements.txt



Test-Driven Development
This project was developed using Test-Driven Development (TDD) principles. All functionality has associated unit tests to ensure correctness and reliability.

The Key Functions Tested:
- calculate_bmi(weight, height): Function to calculate BMI from the user's weight and height.
- get_bmi_category(bmi): Function to classify the BMI value into categories.

*Tests are located in the tests folder under the tests_bmi_calculator.py file.*

Running Tests
The tests are written using Python’s built-in unittest module. To run the tests, use the following command:


python -m unittest discover tests
Example Test Output
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
The tests will automatically validate that the BMI calculation and classification are working as expected.

Contributing
Feel free to fork this repository, make improvements.

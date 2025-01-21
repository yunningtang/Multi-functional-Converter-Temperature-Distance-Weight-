# Multi-functional-Converter-Temperature-Distance-Weight-
# Unit Converter with History Tracking 
## Project Description
This Unit Converter is a Python-based tool that allows users to perform conversions across three categories: length, weight, and temperature. It also allows user to track their history conversions. 

## Build States:

1. **Modular Conversion Functions:**
   Separate functions for length, weight, and temperature conversions. Each function uses a two-step conversion process:
   a. Convert input to a base unit, for example, meters for length, kilograms for weight.
   b. Convert from base unit to the target unit. 

2. **Constant Based Conversions:**
    I defined conversion factors as constants at the beginning of the code. Those conversion factors and formulas used in this project were sources from --> See the **Credit and Resources Section** 

    a. **Length Conversions:** Meters(m) to / from Kilometers (km), Centimeters(cm), Millimeters(mm), Inches, Feet, Miles

    b. **Weight Conversions:** Kilograms(kg) to / from Grams(gm), Pounds(lb), Ounces(oz)

    c. **Temperature Conversions:** Celsius© to / from Fahrenheit(F), Kelvin(K)

    - I use **global constants** to for conversion factors. These constants are defined at the beginning of program and used throughout the whole conversion functions.

3. **Loop and Error Handling:**
    - The main function (converter()) uses a while loop to keep the program running continuously untill they chooses to exit. It will allow user to perform multiple conversions and store them history(dictionary) without restart the program.
    
    - The program will check if the user's input matches valid and menu options. 

    - I also assumed that users may enter units with inconsistent cases (uppercase or lowercase), thus, the program converts user input to a standardized and valid case to ensure the unit conversion function will work properly. 

4. **History Tracking:**
   -  I used a dictionary to store the conversion history. The key for each entry is a conversion counter and will increment with each new conversions. The value is a string which can describe the the input and output units of the conversion.


## Running Instructions 

### Prerequisites
 - Python 3.x installed on the computer.

### Steps to Run the Program
1. Ensure Python is installed.
2. Download the MidtermProject_Riley_Tang.py file
3. Open the terminal or command prompt
4. Run the program following the commands
5. Follow the on-screen prompts to perform conversions, view history, or exit the program. 
### Sample Runs

### Sample Run 1: Length Conversion
This run will demonstrate:
1. A length conversion from meters to feet. 
2. Viewing the conversion history 
3. Exiting the program 
![alt text](image.png)

### Sample Run 2: Temperature Conversion and Error Handling
This run will demonstrate: 
1.	A temperature conversion from Celsius to Fahrenheit
2.	Attempting an invalid conversion (to unit “X”), showing error handling
3.	Viewing the conversion history
4.	Exiting the program 
![alt text](image-1.png)

### Credit and Resources
1.	Length and Weight unit conversions
- Inch Calculator: https://www.inchcalculator.com/convert/
2.	Temperature conversion formulas
- BYJU'S: https://byjus.com/temperature-conversion-formula/

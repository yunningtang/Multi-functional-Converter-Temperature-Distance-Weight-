###################################################################
# University of Toronto
# Faculty of Information
# Bachelor of Information
# INF452: Information Design Studio V: Coding
#
#
#
# Student Name: Riley Tang
# Student Number: 1008977261
#
#
#
# Midterm Project 
# Purpose: The purpose of this program is to converts values between various length, weight, temperature units, and maintains a history of previous conversions. 
# Date Created: Oct. 13, 2024 
# Date Modified: Oct. 20, 2024 
###################################################################
import math
#       Constants for unit conversions
#       Global Variables for Constants
#       Length
M_TO_KM = 0.001                             #       Meters to Kilometers        1 meter = 0.001 kilometers                                                                                                
M_TO_CM = 100                               #       Meters to centimeters       1 meter = 100 centimeters
M_TO_MM = 1000                              #       Meters to millimeters       1 meter = 1000 millimeters
M_TO_INCH = 39.370079                       #       Meters to inches            1 meter = 39.3701 inches
M_TO_FOOT = 3.28084                         #       Meters to feet              1 meter = 3.28084 feet
M_TO_MILE = 0.000621                        #       Meters to miles             1 meter = 0.000621 miles
#       Weight
KG_TO_GM = 1000                             #       Kilograms to grams          1 kilogram = 1000 grams
KG_TO_LB = 2.2046223                        #       Kilograms to pounds         1 kilogram = 2.2046223 pounds
KG_TO_OZ = 35.273962                        #       Kilograms to ounces         1 kilogram = 35.273962 ounces
#       Function to convert length
#       First, convert the input value to meters as our "base" unit for length
def convert_length(value, from_unit, to_unit):
    if from_unit == "km":                      #        If input is in km, divide by km to m factor
        value_in_m = value / M_TO_KM            
    elif from_unit == "cm":                    #        If input is in cm, divide by cm to m factor
        value_in_m = value / M_TO_CM
    elif from_unit == "mm":                    #        If input is in mm, divide by mm to m factor
        value_in_m = value / M_TO_MM        
    elif from_unit == "inch":                  #        If input is in inches, divide by inch to m factor
        value_in_m = value / M_TO_INCH
    elif from_unit == "foot":                  #        If input is in feet, divide by foot to m factor
        value_in_m = value / M_TO_FOOT
    elif from_unit == "mile":                  #        If input is in mile, divide by mile to m factor
        value_in_m = value / M_TO_MILE
    else:                                      #        If input is already in meters, there is no conversion needed
        value_in_m = value

#       Now convert from meters to target unit  
    if to_unit == "km":                        #        Convert meters to kilometers       
        return value_in_m * M_TO_KM
    elif to_unit == "cm":                      #        Convert meters to centimeters
        return value_in_m * M_TO_CM
    elif to_unit == "mm":                      #        Convert meters to millimeters
        return value_in_m * M_TO_MM 
    elif to_unit == "inch":                    #        Convert meters to inches
        return value_in_m * M_TO_INCH       
    elif to_unit == "foot":                    #        Convert meters to feet
        return value_in_m * M_TO_FOOT       
    elif to_unit == "mile":                    #        Convert meters to miles
        return value_in_m * M_TO_MILE
    else:                                      #        Return value in meters if there is no conversion needed
        return value_in_m

#       Now create the function to convert weight
#       param value: The numerical value to convert
#       param value from_unit: The unit to convert from
#       param value to_unit: The unit to convert to
#       then return the converted value 
def convert_weight(value, from_unit, to_unit):
    #       Convert to kg first
    if from_unit == "gm":
        value_in_kg = value / KG_TO_GM         #        Convert grams to kilograms
    elif from_unit == "lb":
        value_in_kg = value / KG_TO_LB         #        Convert pounds to kilograms
    elif from_unit == "oz":
        value_in_kg = value / KG_TO_OZ         #        Convert ounces to kilograms 
    else:
        value_in_kg = value                    #        Assume that input is already in kilograms 

    #       Convert from kg to target unit
    if to_unit == "gm":
        return value_in_kg * KG_TO_GM          #        Convert kilograms to grams
    elif to_unit == "lb":
        return value_in_kg * KG_TO_LB          #        Convert kilograms to pounds
    elif to_unit == "oz":
        return value_in_kg * KG_TO_OZ          #        Convert kilograms to ounces
    else:
        return value_in_kg                     #        Return the value in kilograms if no conversion

#       Function to convert temperature
#       Param value: The numerical value to convert
#       Param from_unit: The unit to convert from (C, F, or K)
#       Param to_unit: The unit to convert to (C, F, or K)
#       return: The converted value
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "C":                
        if to_unit == "F":
            return (value * 9 / 5) + 32             #       Convert Celsius to Fahrenheit
        elif to_unit == "K":
           return value + 273.15                    #       Convert Celsius to Kelvin
    elif from_unit == "F":                  
        if to_unit == "C":
            return (value - 32) * 5 / 9             #       Convert Fahrenheit to Celsius
        elif to_unit == "K":
            return (value - 32) * 5 / 9 + 273.15    #       Convert Fahreheit to Kelvin
    elif from_unit == "K":
        if to_unit == "C":
            return value - 273.15                   #       Convert Kelvin to Celsius
        elif to_unit == "F":
            return (value - 273.15) * 9 / 5 + 32    #       Convert Kelvin to Fahrenheit
    return value                                    #       Return to original value if no conversion needed (same units)

#       Now create main function to run the converte
#       This function input processing, and calls the correct conversion functions
def converter():
    history = {}                                                         #      Dictionary to store the conversion history
    conversion_count = 0                                                 #      Counter for number of conversions

    while True:                                                          #      Main program loop
        print("\n 🔵 Welcome to Unit Converter Tool. ⚪️ ")                #      Welcome Message                   
        print("1. Length")                                               #      Display menu options 
        print("2. Weight")
        print("3. Temperature")
        print("4. View History")
        print("5. Exit")

#       Get user's choice
        choice = input("Enter your choice (1-5):")                        
#       Exit
        if choice == "5":
            break                                                   #       Exit the program if user chooses 5

#       Conversion history
        if choice == "4":                                           
            print("\nConversion History")
            for key, value in history.items():                          
                print(key + ": " + value)                           #       Display conversion history
            continue                                                #       Go back to the start of the loop


        if choice not in ["1", "2", "3"]:
            print("Invalid choice. Please enter the number. ")            
            continue                                                #       Go back to the start of the loop if invalid choice

        value = float(input("Enter the value to convert: "))        #       Get the value to convert           
                             
#       Length Conversion
        if choice == "1":                                           
            print("Available units: m, km, cm, mm, inch, foot, mile")
            from_unit = input("Enter the unit to convert from: ").lower()                                                                                    #       For length conversion, the user is able to shown available units and asked to input the "from" and "to" units
            to_unit = input("Enter the unit to convert to: ").lower()    
#       Added lower(). since the inputs are converted to lowercase for consistency ⬆️
            if from_unit in ["m", "km", "cm", "mm", "inch", "foot", "mile"] and to_unit in ["m", "km", "cm", "mm", "inch", "foot", "mile"]:                  #       ⬇️This checks if both input units are valid lengh units
                result = convert_length(value, from_unit, to_unit)                                                                                           #       If valid, the convert_length function is called with the user
                print(float(value), from_unit, "is equal to", float(result), to_unit)                                                                        #       And then print the result of the conversion
                conversion_count += 1                                                                                                                        #       Also add the count of conversions is incremented, and we will added the previous conversion to the history dictionary, with the count as the key⬇️
                history[str(conversion_count)] = str(float(value)) + " " + from_unit + " = " + str(float(result)) + " " + to_unit
            else:
                print("Invalid units for length conversion.")                               #       Moreover, if either unit is invalid, it will display an error message

#       Weight Conversion
        elif choice == "2":                                                                 #       This block for weight conversions follows the same structure as the length conversion block
            print("Available units: kg, gm, lb, oz")                                        #       Display the available units for weight conversion
            from_unit = input("Enter the unit to convert from: ").lower()                   #       Let the user to enter th units to convert from and to, convertingh inputs to lowercase
            to_unit = input("Enter the unit to convert to: ").lower()

            if from_unit in ["kg", "gm", "lb", "oz"] and to_unit in ["kg", "gm", "lb", "oz"]:                                           #       Check if both input units are valid weight units
                result = convert_weight(value, from_unit, to_unit)                                                                      #       Calls the convert_weight function with the user's inputs
                print(float(value), from_unit, "is equal to", float(result), to_unit)                                                   #       Display the result of the weight conversion
                conversion_count += 1                                                                                                   #       Increments the conversion count
                history[str(conversion_count)] = str(float(value)) + " " + from_unit + " = " + str(float(result)) + " " + to_unit       #       Adds the weight conversion to the history dictionary
            else:
                print("Invalid units for weight conversion.")                                                                           #       Display error message if user inputted invalid input

 #       Temperature Conversion
        elif choice == "3":                                                                                                            
            print("Available units: C (Celsius), F (Fahrenheit), K (Kelvin)")                                                           #       Display available units for temperature
            from_unit = input("Enter the unit to convert from: ").upper()                                                               #       Prompts user to enter the units to convert "from" and "to", converting inputs to uppercase
            to_unit = input("Enter the unit to convert to: ").upper()

            if from_unit in ["C", "F", "K"] and to_unit in ["C", "F", "K"]:                                                             #       Check if both input units are valid temperature units
                result = convert_temperature(value, from_unit, to_unit)                                                                 #       Calls the convert_temperature with the user's inputs
                print(float(value), from_unit, "is equal to", float(result), to_unit)                                                   #       Display the result of the temperature conversion
                conversion_count += 1                                                                                                   #       Increments the conversion counts 
                history[str(conversion_count)] = str(float(value)) + " " + from_unit + " = " + str(float(result)) + " " + to_unit       #       Adds the temperature conversion to history disctionary
            else:
                print("Invalid units for temperature conversion.")                                                                      #       Display error message if user inputted invalid inputs

converter()
#       Calls the function, and starting this program 
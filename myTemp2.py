# Temperature Calculation
import math

# Input temperature
temp = float(input('What is the temp? '))
unit = (input('Is the temp in F or C? ')).strip().upper()

# Lambda functions for conversion
fahrenheit_to_celsius, celsius_to_fahrenheit = lambda temp: 5/9*(temp-32), lambda temp: 9/5*temp+32


# Print the conversions
if unit == 'F':
    print(f"{temp}°F is equal to {fahrenheit_to_celsius(temp):.2f}°C")
elif unit == 'C':
    print(f"{temp}°C is equal to {celsius_to_fahrenheit(temp):.2f}°F")


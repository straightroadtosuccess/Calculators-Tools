# Percentage Calculation
import math

value = float(input('What is this number: '))
total = float(input('Out of this number: '))

percentage = (value / total) * 100
fpercentage = f"{percentage:.2f}"

print(' ')
print('The percentage is: ' + fpercentage)
print(' ')

percent = float(input('What is this percent %: '))
number = float(input('Of this number: '))

result = (percent / 100) * number
fresult = f"{result:.2f}"

print(' ')
print('The result is the number: ' + fresult)
print(' ')

print(' ')
print('And here is some pie 🥧: ' + str(math.pi))
print(' ')

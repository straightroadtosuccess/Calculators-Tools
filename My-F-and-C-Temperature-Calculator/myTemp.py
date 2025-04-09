# Temperature Calculation
import math

ftemp = float(input('What is the temp in F: '))
ctemp = float(input('What is the temp in C: '))

temptoc = (((ftemp - 32) * 5) / 9)
ctc = f"{temptoc:.2f}"
temptof = (((ctemp * 9) / 5) + 32)
ctf = f"{temptof:.2f}"

tempting = ((1 + 2) * 10)

print(' ')
print("C is", ctc)
print(' ')
print("F is", ctf)
print(' ')

'''
Jon Zheng
This program will conver temperatures given in Fahrenheit to Celsius and Kelvin

Pseudocode:
Read the temperature in fahrenheit into temp_fah
set temp_cel = (temp_fah - 32) * (5/9)
set temp_kel = temp_cel + 273.15
print the temperature in Fahrenheit along with the convert temp in Celsius and Kelvin

Input           Output
96               35.5, 308.7
0               -17.7, 255.4
'''
temp_fah = float(input('Enter temperature reading in Fahrenheit '))
temp_cel = (temp_fah - 32) * (5/9)
temp_kel = temp_cel + 273.15

print(f'Temperature reading {temp_fah} in Fahrenheit is {temp_cel} in Celcius and {temp_kel} in Kelvin')
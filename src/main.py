"""
Author : 
Date : 2026-10-19
Version : 1.0
"""

# act06
CONVERSION_RATE = 1.8
celsius = float(input("Enter temp in ºC: "))
# To convert from celsius to farenheit you must multiply by 1.8 and add 32
farenheit = (celsius * CONVERSION_RATE) + 32
print(f"{celsius:.2f} ºC = {farenheit:.2f} ºF")
'''
-------------------------------------------------------------------------------
Name:		practice1.py
Purpose:	Convert fahrenheit to celsius

Author:	Zhou.J

Created:	01/10/2019 
------------------------------------------------------------------------------
'''

# get fahrenheit from user
fahrenheit = float(input("Enter the fahrenheit: "))

# compute celsuis from fahrenheit 
celsius = (5/9)*(fahrenheit-32)

# output celsius 
print("The temperature in celsius is " + str(celsius))

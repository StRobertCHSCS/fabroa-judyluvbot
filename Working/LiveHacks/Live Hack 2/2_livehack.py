'''
*******************************************************************************
Filename:       2_livehack.py
Description:    Determine if user's weight is normal.
Author:         Zhou. D
Created On:     11/18/2019
*******************************************************************************
'''

# get weight and height

weight = float(input("Input your weight (kg): "))
height = float(input("Input your height (m): "))

# calculate Body Mass Index

BMI = weight/(height*height)

# output message

if BMI >= 18.5 and BMI <= 25.0:
    print("Your weight is normal.")
elif BMI < 18.5:
    print("You are underweight.")
else:
    print("You are overweight.")

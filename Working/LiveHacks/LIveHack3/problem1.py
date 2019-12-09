'''
-------------------------------------------------------------------------------
Name:		problem1.py
Purpose:	Figuring out how many heating days there are.

Author:	Zhou.D

Created:	date in 9/10/2019
------------------------------------------------------------------------------
'''

# get amount of days to track
days_tracked = int(input("Enter the number of days to track: "))

# initalize total
total = 0
heating_days = 0

# compute how many heating days
for i in range(days_tracked):
    # get temperature
    temperature = int(input(""))
    if temperature < 15:
        heating_days += 1

# output how many heating days
print("There are " + str(heating_days) + ".")

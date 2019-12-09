'''
-------------------------------------------------------------------------------
Name:		problem2.py
Purpose:	Calculating how long it takes for the uber driver to pass 100km.

Author:	Zhou.D

Created:	date in 9/10/2019
------------------------------------------------------------------------------
'''
# welcome to Distance Tracker
print(" ***** Welcome to the Distance Tracker ******")

# intalize counters
total = 0
days_took = 0

# loop until total reaches 100
while total < 100:
    # compute distance
    distance = int(input("Enter the distance travelled for the day:"))
    total += distance
    days_took += 1

# determine the average distance
average = total/days_took

# output average distance and days took
print("It took " + str(days_took) + " days to surpass 100km driven.")
print("The average distance driven per day is " + str(average) + " km.")

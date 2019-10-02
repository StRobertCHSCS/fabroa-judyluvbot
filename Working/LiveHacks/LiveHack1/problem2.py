'''
-------------------------------------------------------------------------------
Name:		problem2.py
Purpose:	Distribute chicken pieces to students

Author:	Zhou.J

Created:	02/10/2019
------------------------------------------------------------------------------
'''
# get number of students in Mr.Fabroa's class from user
students = int(input("How many students is in Mr.Fabroa's class: "))

# get number of pieces of Popeyes chicken
chicken = int(input("How many chicken pieces are there: "))

# compute how many chicken peices the students will get
chicken_for_students = chicken//students

# compute how many chicken pieces Mr.Fabroa gets
chicken_for_fabroa = (chicken) % students

# output chicken pieces
print("The students get "+str(chicken_for_students)+" each.")
print("The teacher gets "+str(chicken_for_fabroa))

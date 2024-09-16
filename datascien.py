import numpy as np
from pandas.core.interchange.from_dataframe import categorical_column_to_series

my_list = [1,2,3]

arr = np.array(my_list)
print(type(arr))
print(arr)

#two-dimensional array
my_mat = [[1,2,3],[4,5,6],[7,8,9]]
print(np.array(my_mat))
print(type(np.array(my_mat)))

#arange will give number in the first and last digit.
# and it even has a step as well
print(np.arange(0,10,2))

#np.zero will give the matrix with 0's
#similarly we have np.one to get matrix full of 1's
print(np.zeros((3, 3)))
print(np.ones((2,2)))


#we have linspace where it has a start and end and a sep in which
#its work is to divide the range into the step number.
print(np.linspace(0,5,10))

def new_name(fname, lname):
    '''this is going to take the first adn last name of the user and formate it and return as title case'''
    formate_fname = fname.title()
    formate_lname = lname.title()
    return print(f"this is your firstname: {formate_fname} and your last {formate_lname}")

new_name('Saran joel', 'Marrikanti')

def my_function(a):
    if a<40:
        return print('terrible')
    if a<80:
        return "pass"
    else:
        return 'great'

my_function(5)


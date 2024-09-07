'''write a python program to read information of student froma csv file and create a json object
so in the end we will have an array of json object'''

#the csv file contain student_id, student_name, student_address.

import pandas as pd
from pandas import *

df = read_csv('Book1.csv')
json_array = df.to_json(orient='records' , indent=4)
print(json_array)
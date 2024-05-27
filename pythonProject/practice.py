'''
Data Types
'''
#String

#integer
print(123_3434_323)

#float is for decimal places like 3.14159

#boolean
True
False #they should start with Initial

#len()#len function cannot work for integer it gives error

# num = len(input("enter the name"))
# print(f"your name has{num} numbers")
#print("name has"+num+ "characters")  you cannot concatenate a string and integer

# two_digit_num= input()
# add= int(two_digit_num[0]) + int(two_digit_num[1])
# print(add)

'''
Welcome to tip calaculator
what was the bill   ?
How much tip would you like to give 10 12 or 15
how many people to split the bill?
each person should pay : this much
'''

#Variables
# bill - float
# tip - Int
#billwith_tip
# Split_bill - float
#paybill = float

bill = float(input("What was the bill?"))
tip = int(input("How much tip would you like to give 10 12 or 15"))
billwith_tip = (tip/100 *bill) + bill
split_bill = int(input("Among how many people tp slit the bill?"))

paybill = billwith_tip/split_bill
print(f"each person should pay{round(paybill,2)}")

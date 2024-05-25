"""this is multiline comment

Date ; 2024-05-21

Variable : its a temporary memory allocation in the RAM to hold information. For processing
types of Variable: int, float (double), boolean
string :collection of characters in sequence, it is immutable



a = 5 #it is int
b = 55.6 # it is float
c= True # it is boolean
d='Saran Joel' # it is string

a =input('enter the name you want\n')
print('your name is ',a)

result = input('enter the vaue to be double')
result1 = result*2
print('the number ofter double is ',result1)

print(type(result1))
print(type(result))
print(a*b)
"""

name = 'Saran Joel'
age = 100
money = 1039847565


####### STRING FORMATION ########
print( 'my name is',name,'my age is ', age,'i have', money,'much money')  # this is string fromating
#formate one script
print('my name is %s and i am %d and i have %f money'%(name, age, money)) # this is string formating

print('my name is {} and my age is {} and i have {} money'.format(name, age, money) )

print(f'my name is {name} and my ae is {age} and  i have {money} this much money')

print(5/2) # the result is float
print(5//2) # the result is interger
print(type(5//2))
# CReate a program to calculate sum and avg of 3 numbers

n1 = float(input("enter number 1: "))
n2 = float(input("enter number 2: "))
n3 = float(input("enter number 3: "))

add = n1+n2+n3
print(f'the sum of {n1} {n2} {n3} is {add}')

"""
Documentation : 1)internal (Comments) 2) external
triple quotation is for multi-line comments /* */
Topic : IPO --> input/process/output
Date : 2024-05-21
Author : Hesam Akbari

Variable in programming : its  memory allocation
in the RAM to hold information temp. for processing
Type variables : int, char, float (double), boolean
string! -> char
# data structure -> collection of data
1) string (txt) : collection of character in sequence, immutable
# ALL THE INPUT AND OUTPUT OF ANY PROGRAMMING LANGUAGES ARE IN FORM OF
# STRINGS  "Hesam"  "maeHa"
7 -->  0000 0111
int a = 78

a = 5  # int
b = 56.3 # float
c = True
d = 'Hesam'
# variable in python are dynamic
print(type(a))
print(type(b))
print(type(c))
print(type(d))

a = 5
b = 2
c = "5"
d = "2"
print(a + b)
print(a * b)
print(c + d)  # string concatenation
#print(c * d) # TypeError: can't multiply sequence by non-int of type 'str'
print(a * d)
# int() # float() # bool() # str()
print(int(True))
print(float(True))
print(bool(5))
#  ------------------------- Input -----------------
print() # prompt to the user
name = input("Enter your name :\n")
print('your name is ', name)
age = int(input("Enter your age and I'll double it"))
result = age * 2
print('the result is', result)
print(age * 5)
"""
#  ----------------------- ouput -------------------
name = "hesam"
age = 40
money = 240.65
print(name, age, "Hello", sep=" (❁´◡`❁) ", end="||\n")
print(money)
# string formating
print("My name is Hesam and I am 40 years old and I have 24.65 dollars")
print("My name is", name, "and I am", age, "years old and I have", money, "dollars")
print("My name is %s and I am %d years old and I have %.2f dollars" % (name, age, money))
print("My name is {} and I am {} years old and I have {} dollars".format(name, age, money))
print(f"My name is {name} and I am {age} years old and I have {money:.1f} dollars")

# ------------------------------------ create a program to calculate sum and avg of 3 numbers
a = input("Enter a number") # defensive exception handling
if a.isdecimal():
    print(a)
else:
    print('bad input')

# input validation...
try:
    num1 = float(input('Enter the first number : '))
    num2 = float(input('Enter the second number : '))
    num3 = float(input('Enter the third number : '))
    add = num1 + num2 + num3
    print(f'The sum of {num1}, {num2}, {num3} is {add} and avg is {add/3:.2f}')
except ValueError :
    print('bad input!')
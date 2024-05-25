# '''
#
# Boolean
# Decision-making
# 1.if statement - single line statement
# 2.if-else statement - dual line statemetn
# 3.if-else-then statement- nested
#
#
# Recursion Loops
#
# '''
#
# a=10
#
# b = 5
# if (a>b):
#     print('a is greater than b')
# while (a>b):
#     print('hello')
#     b += 1


#
# first_number = int(input('enter 1'))
# second_number = int(input('enter 2'))
# third_number = int(input('enter 3'))

# for i in range(first_number, second_number):
#     i += 3
#     print(i)
#     cube = first_number ** 3
#
#     print(f'{first_number} cubed is {cube}')

a = int(input('1st number'))
b = int(input('2nd number'))
c = int(input('3rd number'))

for i in range(a,b,c) or range(b,a,c):
    cube = i **3
    print(f'{i} cubed as {cube}')


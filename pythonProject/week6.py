"""
IPO
Decision-MAking
Loops(while for)
Functions and modules
Menu Driven - Modularization
Data Structure --> it is a collection of data
1. Strings
2.List
3.Tuples
4.Dictionaries
5.sets
6.Class
"""
alist = [1,2,2,2,2,2,3,4,3,5,1,2,2,9]
redunlist = []
for item in alist:
    if item not in redunlist:
       redunlist.append(item)
print(redunlist)

"""
IPO
Decision-making
Loops (while, for)
Functions and modules
Menu-driven --> Modularization
Data Structures --> it's a collection of data (corrected)
1) string : collection of character in sequence, immutable (Read Only)
Arrays : collection of same type data in sequence, mutable
FIXED data struction ---> import numpy --->Arrays
2) list : collection of items in sequence, mutable, dynamic
3) Tuples
4) Dictionaries
5) sets
6) Class
"""
# index = size - 1
name = "hesam akbari"
alist = [1, 2, 3, 4, 6, 10]
aMixList = [1, 3.4, True, 'hesam']
# for i for(int i =0 ; i < length ; i ++)
for ch in name:  # for each iterator!
    print(ch, end='-')
print()
print('---------------------')
for i in range(len(name) - 1, -1, -2):  # [0,1,2,3,...11]
    print(name[i], end="*")
print()
for number in alist:
    print(number, end='-')
print()

print('size ', len(name))
print('first', name[0])
print('last', name[-1])
print('size ', len(alist))

# --------------------------------------------------------
# how do I create an empty list!
alist = []
alist2 = list()
print(alist, alist2)
name = 'Hesam'
# name[0] = 'w' # 'str' object does not support item assignment
name = list(name)
print(name)
name[0] = 'w'.upper()
print(name)
name = ''.join(name)
print(name)

# -------------------------------- sublist -----------------
alist = [2, 3, 4, 5, 6, 7, 8, 9, 11]
alistR = alist[::-1]  # start (b): stop(end): step(1)
print(alist)
print(alistR)
print(alist[:4:-1])
print(alist[4::])
#  ------------------------------ useful function for list manipulation ----
alist = []
# --------------- adding items to list ----------------------
alist.append(5)  # one object (item) at time to the list
print(alist)
alist.append(10)  # one object (item) at time to the list
print(alist)
alist.append(11)  # one object (item) at time to the list
print(alist)
alist.append(12)  # one object (item) at time to the list
print(alist)
alist.insert(1, 100)  # added
print(alist)
#alist =[0] * 10 # declarion of array size 10
dummy = [1, 2, 3, 4]
for n in dummy: alist.append(n)
print(alist)
alist.extend('hesam')
print(alist)
alist.append('x')
# ---------------------------- remove ------------------
last = alist.pop(1)  # remove and return the last item by default
print(last)
print(alist)

if 'x' in alist:
    print('index of x', alist.index('x'))

alist.remove('h')  # remove value!
print(alist)

alist2 = alist.copy()

alist2[2] = 1000
print(alist[2])
alist = [1, 2, 2, 2, 2, 3, 4, 3, 5, 1, 2, 2, 9]
print(alist.count(2))

alist2 = []
for number in alist:
    if number is not alist2:
        alist2.append(number)
# -------------------------- write a code to remove all the redundancies
# from this list (DO NOT USE SET!)
index = 0
while index < len(alist):
    if alist.count(alist[index]) > 1:
        alist.pop(index)
    else:
        index += 1

print(alist)


#
#
# this is to test when will the for loop exit
total = 0
max = int(input('enter max money yuo want to spend'))
for count in range(1, 11):
    cost = int(input('Enter the cost of item'))
    total = total + cost
    if total > max:
        print('you have reached your limit')
        total = total - cost
        break
    print(f'you have brought{count} items')
print(f'your total is {total}')
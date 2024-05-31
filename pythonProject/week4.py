'''
functions are modules
we are already using function
they are [redefined
they can be Black box or pre-defined means we dont know what we are going to define in it like - print() input()

we also have white box or self defined
'''
def message(a):
    print(f"this is ht evlaueof {a}")
    print('Hello this is a message funciton')

message(10)



v =2
def value():
    global v
    v = 5
    result = v*2
    print(v)
    print(result)
    return

print(v)
value()
print(v)

#Nested functions in other


def demo():
    value = 2
    def demo1():
        value=3
        print(value)
    def demo2():
        value=4
        print(value)
    def demo3():
        value=5
        print(value)

    demo1()
    print(value)
    demo2()
    print(value)
    demo3()
    print(value)
print(value)
demo()
print(value)

#modulization in programing
#Collect 3 integers and print sum an avg of 3
# first of computationl thinking for developing a program
'''
1.collect the three input 
2.calaculate teh sum 
3.calaculate avg
4.showresult
'''

def collectInput():
    global  n1,n2,n3
    n1 =int(input('enter the number 1'))
    n2 = int(input('enter the 2nd number'))
    n3 = int(input('enter the 3rd number'))
def calculateSum():
    return n1+n2+n3
def calculateAvg():
    return calculateSum()/3
def showResult(sum,avg):
    print(f"the result of{n1}, {n2}, and {n3} sumation is {sum} and their avg is {avg}")



def main():
    collectInput()
    sum = calculateSum()
    avg = calculateAvg()
    showResult(sum, avg)

main ()
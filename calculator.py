'''this is calcualtor project where i used functions and used recursive function i.e used a function inside that function'''
def add(num1, num2):
    return num1 + num2;


def sub(num1, num2):
    return num1 - num2;


def multiply(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


operations = {
    '+': add,# we can use functions as a variable value. To do that it should not be in--> '()' parenthesis
    '-': sub,
    '*': multiply,
    '/': div
}


def calculator():
    option = True;
    num1 = float(input("what is your first number: "))

    while option:
        for operators in operations:
            print(operators)
        operative_symbols = input('Pick an operations')
        num2 = float(input('enter your second number: '))
        operation = operations[operative_symbols](num1, num2)# this is s way to access dictonary
        choice = input(f"type Y to continue with {operation} or N to Start new")

        if choice == "Y":
            num1 = operation
        else:
            option = False
            print("\n" * 5)
            calculator()#this is a recursive function. im using same function as it is


calculator()
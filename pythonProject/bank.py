'''

this should have

def deposit money
def with draw money
def check balance
def show menu

it should have show menu where it has all the
other def in it for here the user chooses which action
to take from his prefernce

like choosing a number

def show menu
'''

#these are global varibales that are used in the functions
amount = 0 #amount for storing the deposit amount
userName = '' #this is to take the name of the user
def depositMoney():
    #declaring teh variables as global
    global amount
    global userName
    #while true perform the deposit transaction
    while True:
        try:#using try expect to handel error
            depMoney = int(input(f'{userName} enter the money you want to Deposit:$ '))
            if depMoney > 0:#checking the condition and making the transaction
                amount += depMoney
                print(f'{userName} you have deposited ${depMoney}')
                print(f'your Current balance is ${amount}')
                return amount
            else:#if error this will be shown
                print(f'please enter correct amount')

        except ValueError:#if the input not what we expect this is shown
            print('Please enter the proper amount to deposit')



def withdrawMoney():
    #declaring the variables as global so that we can use them as they already have value
    global amount
    global userName
    while True:
        try:#using try expect to handel errors
            wMoney = int(input(f'{userName} Enter the amount you want to withdraw:$'))
            if  amount >= wMoney:#if the mount that want to withdraw is greate than the savings this is true
                amount -= wMoney
                print(f'{userName} you have withdrawn ${wMoney}')
                return amount
            else:#if not then this is printed
                print('Insufficient Funds ')
                print(f'Your Balance is ${amount}, First deposit amount to withdraw')


        except ValueError:#this is used to expect error
            print('INVALID INPUT')


def displayBalance():
    #varianles are delared as global so that they can be used
    global amount
    global userName
    print(f'{userName} Your current balance in your account is ${amount} ')

def menu():
    global userName
    print('=============Welcome to Bank============')
    print('1. Deposit Amount')
    print('2. Withdraw Amount')
    print('3. Check Balance')
    print('4. Exit')
    return input(f'{userName} Enter 1, 2, 3, or 4 to proceed with your Transaction:')#here we are taking the input and returing it

def showMenu():
    global userName
    while True:
        #here teh name of the customer is take and if customer did not it will give else statement
        userName = input('Dear Customer Enter your Name:').strip()
        if userName :
            break
        else:
            print('Name cannot be Empty!!!')
#here the process happens where the input is match and use for calling appropriate fucntion
    while True:
        match = menu()
        if match == '1':
            depositMoney()
        elif match == '2':
            withdrawMoney()
        elif match == '3':
            displayBalance()
        elif match == '4':
            print('You have ended your Transaction and exited from you account')
            return
        else:
            print('Please enter a valid key to proceed with your Transaction')


showMenu()
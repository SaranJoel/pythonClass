'''
IPO ----> Decision making, loops----> functions
APIs ----> packags ----> libraries

menu-driven programming
'''
import pyjokes

# import math
# import pyjokes
# print(pyjokes.get_joke())
#
# print(math.pi)
# print(math.factorial(5))


'''
we can do the above import like this as well
as from math import * ---> for importing all the in side the math package

from maht import pi, factorial ----. this is like importing a specific API
'''

# -------------------Guessing game-----------
# a user supposed to guess a randomm number b/w 1 to 100
# computer provided feedback and let the user guess to find that number
# and count how many times you took to find the number
# if you guess something smaller =---> guess something bigger\
# if you guess something bigger =---> guess soemthng samller

import random


def guessingGame():
    ranNum = random.randint(1, 100)
    lower, upper = 1, 100
    count = 0
    while True:
        userInput = int(input(f'Enter the number you want to guess b/w {lower} and {upper}'))
        count += 1
        if ranNum > userInput:
            print('Guess some thing bigger')
            lower = userInput
        elif ranNum < userInput:
            print('Guess something smaller')
            upper = userInput
        else:
            print(f'your game is over with the count of{count}')
            return count

def menu():
    print('=========Guessing Game===========')
    print('1 - Single Player')
    print('2 - Two Player')
    print('3 - Tell me a Joke!')
    print('4 - Exit the program')
    print('----------------------------------')
    return input('Enter 1, 2, 3, or 4:')


def guessingGameTwoPlayer():
    """
       two players compete over one random number. Players guess alternatively and whoever find the number
       first is the winner. program still provide feedback to help the players find the number
       Hint : 1) you should collect the players name !
       2) since whoever start the game first has disadvantage over other player. we should pick who start the
       game randomly!
       3) *** you should dedicate a variable to keep track of the turns and change it accordingly...
       30 min --->

       """
    ranNum = random.randint(1, 100)
    p1 = input('Enter the name of player 1:')
    p2 = input('Enter the name of player 2:')
    if random.randint(0, 1):
        turn = p1
    else:
        turn = p2
    lower, upper = 1, 100
    while True:
        userInput = int(input(f"{p1} Enter the number b/w {lower} and {upper}"))
        if ranNum > userInput:
            print('Enter a something bigger')
            lower = userInput
        elif ranNum < userInput:
            print('Enter a something smaller')
            upper = userInput
        else:
            print(f"---> Game winner is {turn}")
            return
        # this is to chnage the turn of the player

        if (turn == p1):
            turn = p2
        else:
            turn = p1


def gameEngine():
    while True:
        match = menu()
        if match == '1':
            guessingGame()
        elif match == '2':
            guessingGameTwoPlayer()
        elif match == "3":
            print(pyjokes.get_joke())
        elif match == '4':
            print('thanks for playing GoodMF!!')
            return
        else:
            print('bad input, play properlyMF!!!')


gameEngine()

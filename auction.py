'''1. first to ask the name of the  bidder
2. ask the bidder how much he is going to bid and store it
3.ask if there are any other bidders  YES or NO'''

#this is the  welcome statement
print('Welcome to the secrete Auction program')

#this is an empty dictionary
data = {}
#this is true until it meet the condition and it will run like a loop,
#until the if condition is made true and triggers the break of this if statement.
while True:
    name = input("What is your name?:")
    bid  = int(input("What is your bid?:"))

    condition = input("Are there any other bids? Type 'yes' or 'no'.")
    data[name] = bid
    if condition == 'no':
        break;


#print(data)
compare = max(data, key=data.get)#here the value of thkeys is compared
print(f' the highest bidder {compare} and the bid is {data[compare]}')


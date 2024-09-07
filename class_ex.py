class Item:
    def __init__(self):

        print("this is init method and it is called when ever the Item class is called")

    def calcu_total_price(self,name, price, quan):
        print(f"the name is {name}, and the price of {quan} pieces is {price}")

item = Item()
item.name = "Saran"
item.price = 100
item.quantity = 2
#item.calcu_total_price(item.name, item.price, item.quantity)

item1 = Item()
item1.name = "joel"
item1.price = 230
item1.quantity = 4


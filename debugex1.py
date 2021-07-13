user_funds = 10.31
price = {"Burger":5.00,"Pasty":3.20}
item_price = price["Burger"]#8.00 

if item_price < user_funds:
    print("You have enough money!")
elif item_price == user_funds:
    print("You have the precise amount of money")
elif item_price > user_funds:
    print("Sorry you don't have enough money")
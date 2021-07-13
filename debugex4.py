import pdb
pdb.set_trace()


item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0
i = 0

while n < 5:
    for item_name in item_list:
        print("Item " + str(n+1) + " is " + item_name)
        n = n + 1

print("Last item in list is " + item_list[len(item_list)-1])
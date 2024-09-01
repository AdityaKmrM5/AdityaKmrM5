#Hotel Menu
menu = {
    'Burger':99,
    'Pizza':150,
    'Litti-chokha':300,
    'Coffee':70,
    'Water-bottle':20,
    'Tea':15
    
}

#greeting
print("welcome to Aditya's hotel")
print("Burger: Rs99\nPizza: Rs150\nLitti-chokha: Rs300\nCoffee: Rs70\nWater-bottle: Rs20\nTea: Rs15")

#Order_total
order_total = 0

item_1 = input("Enter the name of item you want to order=")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item{item_1} has been added to your order")

else:
    print("ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order.lower() == "yes":
        item_2 = input("Enter the name of second item = ")
        if item_2 in menu:
            order_total += menu [item_2]
            print(f"Item {item_2} has been added to your order")
        else:
            print(f"ordered item {item_2} is not available!")

print(f"The total amount of items to pay is {order_total} ")
    
print("Thank You")

print("Visit Again")

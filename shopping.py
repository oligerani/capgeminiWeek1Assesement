items = {}

def add_item(name, price):
    items[name] = price

def view_cart():
    if items:
        for name, price in items.items():
            print(f"Item: {name}, Price: {price}")
    else:
        print("Your cart is empty.")

def total_price():
    total = sum(items.values())
    print(f'Total price in cart is {total}')
        
while True:
    choice = int(input(' 1.Add Item \n 2.View cart Item \n 3.Calculate total price \n 4.Exit \n Enter the choice ='))
    
    if choice == 1:
        name = input('Enter name of Item = ')
        price = int(input('Enter price of item = '))
        add_item(name, price)
    elif choice == 2:
        view_cart()
    elif choice == 3:
        total_price()
    else:
        break
# Hotel Menu
menu = {
    'pizza': 120,
    'burger': 80,
    'salad': 60,
    'pasta': 100,
    'coffee': 40,
}

print("Welcome to our hotel!")
print("\nHere is our menu:")

for item, price in menu.items():
    print(f"{item}: Rs{price}")

order_total = 0
orders = {}

while True:
    item = input("\nEnter the item you would like to order: ").lower()

    if item in menu:
        quantity = int(input(f"How many {item}s would you like? "))

        cost = menu[item] * quantity
        order_total += cost

        if item in orders:
            orders[item] += quantity
        else:
            orders[item] = quantity

        print(f"{quantity} {item}(s) added to your order.")
        print(f"Current total: Rs{order_total}")

    else:
        print("Sorry, that item is not available.")

    another_order = input("Would you like to order anything else? (yes/no): ").lower()

    if another_order != "yes":
        break

print("\n========== BILL ==========")

for item, quantity in orders.items():
    item_cost = menu[item] * quantity
    print(f"{item.capitalize()} x {quantity} = Rs{item_cost}")

print("--------------------------")
print(f"Total Amount: Rs{order_total}")
print("Thank you for dining with us!")
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

while True:
    item = input("\nEnter the item you would like to order: ").lower()

    if item in menu:
        order_total += menu[item]
        print(f"{item} added to your order.")
        print(f"Current total: Rs{order_total}")
    else:
        print("Sorry, that item is not available.")

    another_order = input("Would you like to order anything else? (yes/no): ").lower()

    if another_order != "yes":
        break

print("\n----- BILL -----")
print(f"Total amount to pay: Rs{order_total}")
print("Thank you for dining with us!")
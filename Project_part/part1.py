
cafe_name = "The Daily Tea"
tax_rate = 0.08

menu = {
    "espresso": 2.00,
    "latte": 3.00,
    "boba": 4.05,
    "herbal tea": 4.50,
    "chocolate chip muffin": 2.50,
    "chicken wrap": 3.25,
    "vegan wrap": 3.75,
}

order = []


# Welcome the customer
def greet_user(name):
    print(f"Hello {name}, Welcome to {cafe_name}!")


name = input("Enter Your name: ")
greet_user(name)


# Displayind the cafe menu
def show_menu(menu):
    print("---- MENU---- ")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")


# To Display the order
def show_order(order, menu):
    if len(order) == 0:
        print("Your cart is empty")
    else:
        print("\n HERE IS YOUR ORDER ")
        for item in order:
            print(f"{item}: ${menu[item]:.2f}")


# Calculate subtotal
def calculate_subtotal(order, menu):
    subtotal = 0

    for item in order:
        subtotal += menu[item]

    return subtotal


# Rewards membership
user_member = input(
    "Are you a Rewards Member? yes/no: "
).lower()

user_member = user_member == "yes"


# Calculate discount
def discount(subtotal, user_member):

    if user_member and subtotal >= 20:
        discount_amount = subtotal * 0.15

    elif user_member and subtotal >= 10:
        discount_amount = subtotal * 0.10

    elif not user_member and subtotal >= 25:
        discount_amount = subtotal * 0.05

    else:
        discount_amount = 0

    return discount_amount


# Printing the receipt
def receipt(name, order, menu, user_member):

    subtotal = calculate_subtotal(order, menu)
    discount_amount = discount(subtotal, user_member)

    discounted_subtotal = subtotal - discount_amount

    tax = discounted_subtotal * tax_rate

    total = discounted_subtotal + tax

    print(f"\n {cafe_name} RECEIPT ")
    print(f"Customer: {name}")

    for item in order:
        print(f"{item}: ${menu[item]:.2f}")

    print("----------------------")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount_amount:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")

    if not user_member:
        print("\nJoin our Rewards Program!")

    print("Have a great day and thank you!")


# Main ordering system
while True:

    print("\n1. View menu")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. View my order")
    print("5. Checkout")

    user_options = input("Choose an option (1-5): ")

    # View menu
    if user_options == "1":
        show_menu(menu)

    # Adding an item
    elif user_options == "2":

        which_item = input("Adding which item?: ").lower()

        if which_item in menu:

            try:
                quantity = int(input("How many?: "))

                if quantity <= 0:
                    print("Please enter a quantity greater than zero.")
                    continue

                for i in range(quantity):
                    order.append(which_item)

                print("ADDED")

            except ValueError:
                print("Please enter a valid number.")

        else:
            print("Sorry, that item is not on the menu.")

    # Removing an item
    elif user_options == "3":

        which_item = input("Removing which item?: ").lower()

        if which_item in order:

            try:
                quantity = int(input("How many?: "))

                if quantity <= 0:
                    print("Please enter a quantity greater than zero.")
                    continue

                if order.count(which_item) >= quantity:

                    for i in range(quantity):
                        order.remove(which_item)

                    print("REMOVED")

                else:
                    print("You don't have that many in your cart.")

            except ValueError:
                print("Please enter a valid number.")

        else:
            print("That item is not in your order.")

    # View order
    elif user_options == "4":
        show_order(order, menu)

    # Checkout
    elif user_options == "5":

        if len(order) == 0:
            print("Your cart is empty. Please add something first.")

        else:
            receipt(name, order, menu, user_member)
            print("Thank you for visiting the Daily Tea!")
            break

    # Invalid option
    else:
        print("Invalid option. Please choose from 1-5.")

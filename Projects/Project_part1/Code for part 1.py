cafe_name = "The Daily Tea"
tax_rate = 0.08

menu = {
    "espresso": 2.00,
    "latte": 3.00,
    "boba": 4.00,
    "herbal tea": 4.50,
    "chocolate chip muffin": 2.50,
    "chicken wrap": 3.25,
    "vegan wrap": 3.75,
}

order = []

def greet(name):
     print(f"Hello {name}, Welcome to {cafe_name} ")
name= input("Hello Costumer!, Please Enter Your name: ")
greet(name)

is_member= input("Are you a Rewards Member? yes/no: ").lower()=="yes"

def show_menu(menu):
    print("``````MENU``````")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")


    

def show_order(order, menu):
     if len(order)==0:
          print("Your cart is empty")
     else:
        print("HERE IS YOUR ORDER")
        for item in order:
            print(f"{item}: ${menu[item]:.2f}")
        print(f"Items: {len(order)}")

def calculate_subtotal(order, menu):
    subtotal = 0
    for item in order:
        subtotal += menu[item]
    return subtotal



def get_discount(subtotal, is_member):
    if is_member and subtotal >= 20:
        discount_amount = subtotal * 0.15
    elif is_member and subtotal >= 10:
        discount_amount = subtotal * 0.10
    elif not is_member and subtotal >= 25:
        discount_amount = subtotal * 0.05
    else:
        discount_amount = 0

    return discount_amount


def print_receipt(name, order, menu, user_member):
    subtotal = calculate_subtotal(order, menu)
    discount_amount = get_discount(subtotal, is_member)
    discounted_subtotal = subtotal- discount_amount
    tax = discounted_subtotal*tax_rate
    total = discounted_subtotal+ tax

    print(f"{cafe_name} RECEIPT")
    print(f"Customer: {name}")

    for item in order:
        print(f"{item}: ${menu[item]:.2f}")

    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount_amount:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")

    if is_member != "yes": #!= saying that it is not equal to yes
        print("Join our Rewards Program!")

    print("Have a great day, and thank you for shopping!")

    return total

while True:
     print("1. View menu")
     print("2. Add an item")
     print("3. Remove an item")
     print("4. View my order")
     print("5. Checkout")

     user_options= input( "Choose an option (1-5):  ")
     
    
     if user_options == "1":
        show_menu(menu)
          

     elif user_options == "2":
        item = input("What would you like to order? ").lower()

        if item in menu:
            quantity = int(input("How many? "))

            if quantity >= 1:
                for i in range(quantity):
                    order.append(item)
            print(f"Added {quantity} {item}(s) to your order")
            if quantity== 0:
                print("Choose at least 1 item.")

        if item not in menu:
                print("This item is not in our menu.")

     elif user_options == "3":
        which_item = input("Which item would you like to remove? ").lower()
        if which_item in order:
            order.remove(which_item)
            print(f"{which_item} has been removed from your order.")
        else:
            print(f"{which_item} isn't in your order.")


        
     elif user_options == "4":
        show_order(order, menu)
          
     elif user_options == "5":
        
        if len(order) == 0:
            print("Your order is empty. Please add something before checking out.")

        else:
            print_receipt(name, order, menu, is_member)
            break

     else:
        print("Please choose from (1-5)")



     

        




    
   

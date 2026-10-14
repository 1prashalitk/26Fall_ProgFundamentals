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

def greet_user(name):
     print(f"Hello {name}, Welcome to {cafe_name} ")
name= input("Hello Costumer!, Please Enter Your name: ")
greet_user(name)


def show_menu(menu):
    print("-MENU-")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")


    

def show_order(order, menu):
     if len(order)==0:
          print("Your cart is empty")
     else:
        print("HERE IS YOUR ORDER")
        for item in order:
            print(f"{item}: ${menu:.2f}")
        print(f"Items: {len(order)}")

def cal_subtotal(order, menu):
     for item in order:
        subtotal= menu[item]
     return subtotal


user_member= input("Are you a Rewards Member? yes/no: ").lower()

def discount(subtotal, user_member):
     if user_member and subtotal >= 20:
          discount =subtotal*0.15
     elif user_member and subtotal >=10:
          discount= subtotal*0.10
     elif not user_member and subtotal >=25:
          discount= subtotal*0.05
     else:
          discount=0
     return discount
def receipt(name,order,menu, user_member):
     cal_subtotal(order,menu)
     discount(cal_subtotal, user_member)
     discounted_subtotal= cal_subtotal- discount
     total= discounted_subtotal + tax_rate
     return total

     print(" {cafe_name} RECEIPT " )

     for item in order:
          print(f"{item}: ${menu[item]}:.2f")

     print(f"Subtotal: ${cal_subtotal:.2f}")
     print(f"Discount: -${discount:.2f}")
     print(f"Tax: ${tax_rate:.2f}")
     print(f"Total: ${total:.2f}")

     if not user_member:
          print("Join our Rewards Program")
          print(" Have a greet day and Thank You for shopping!")

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

     elif user_options == "3":
            which_item= input("Removing which item?: ")
            if item in menu:
                quantity=input("How many?: ")
            if item in order:
                order.remove(item)
            print(f"Removed {item} from your order")
          
     elif user_options == "4":
        show_order=(order, menu)
          
     elif user_options == "5":
        receipt(name,order,menu, user_member)
     elif user_options >"5":
        print("Please choose from (1-5): ")
        



    
   

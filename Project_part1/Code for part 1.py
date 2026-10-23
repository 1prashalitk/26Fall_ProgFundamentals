cafe_name = "Python Café"
tax_rate = 0.08

menu ={
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
user_input= input("Enter Your name: ")
greet_user= (user_input)
print(f"Hello {greet_user}, Welcome to the Python Cafe!")


def show_menu(menu):
    print(" MENU ")
    for item, price in menu:
        print(f"{item}: ${price:.2f}")

def show_order(order, menu):
     if (order)==0:
          print("Your cart is empty")
     else:
          print("HERE IS YOUR ORDER")

def Calculate_subtotal(order,menu):
     for item in order:
          subtotal+= menu[item]
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
     subtotal= Calculate_subtotal(order,menu)
     discount= discount(subtotal, user_member)
     discounted_subtotal= subtotal- discount
     tax= discounted_subtotal + tax_rate
     total= discounted_subtotal + tax_rate

     print(" {cafe_name} RECEIPT " )

     for item in order:
          print(f"{item}: ${menu[itme]}:.2f")

     print(f"Subtotal: ${subtotal:.2f}")
     print(f"Discount: -${discount:.2f}")
     print(f"Tax: ${tax_rate:.2f}")
     print(f"Total: ${total:.2f}")

     if not user_member:
          print("Join our Rewards Program")
          print(" Have a greet day and Thank You for shopping!")

while True:
     print("\n1. View menu")
     print("2. Add an item")
     print("3. Remove an item")
     print("4. View my order")
     print("5. Checkout")

     user_options= input( "Choose an option (1-5):  ")

    

     if user_options == "1":
          show_menu(menu)
     if user_options == "2":
          which_item= input("Adding which item?: ")
          quantity= input("How many?: ")
          print("ADDED")
     elif user_options == "3":
          which_item= input("Removing which item?: ")
          quantity=input("How many?: ")
          print("REMOVED")
     elif user_options == "4":
          print("Here is your order")
     elif user_options == "5":
          receipt= receipt(name,order,menu, user_member)




    
   



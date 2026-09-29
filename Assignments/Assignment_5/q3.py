def check_number(number):
    if number%2==0: #even only if the number is divisible by 2 using the if statements
        return "even" # if the number is even it will be returned even
    else:
        return "odd" #  if the number is odd it will be returned odd
number=int(input("Enter a whole number: ")) #asking the user for whole number
final= check_number(number) #final is a variable for the check_number
print(f"{number} is an {final} number")

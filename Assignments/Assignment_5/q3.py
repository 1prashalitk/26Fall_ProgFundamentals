def check_number(number):
    if number%2==0: #even only if the number is divisible by 2
        return "Even" # if the number is even it will be returned even
    else:
        return "Odd" #  if the number is odd it will be returned odd
number=int(input("Enter a whole number: ")) #asking the user for whole number
result= check_number(number)
print(f"{number} is an {result} number")

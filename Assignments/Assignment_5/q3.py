def check_number(number):
    if number%2==0:
        return "Even"
    else:
        return "Odd"
number=int(input("Enter a whole number: "))
result= check_number(number)
print(f"{number} is an {result} number")

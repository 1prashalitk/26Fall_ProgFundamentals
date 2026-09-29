def rectangle_stats(length, width):
    area = length*width # area formula
    perimeter = 2*(length + width) #perimeter formula
    return area, perimeter

length = float(input("Enter the length: ")) #asking the user for length
width = float(input("Enter the width: "))  #asking the user for width

area, perimeter = rectangle_stats(length, width)

print(f"Area: {area:.2f}") # the :.2f to make it round to 2 decimals 
print(f"Perimeter: {perimeter:.2f}")

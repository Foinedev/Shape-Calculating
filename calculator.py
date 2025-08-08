import math #To use pi later
used = 0
#Title
print("""
====================
  Area Calculator📐
=====================
""")
print("Choose a shape")
shape=input("""
1. Square
2. Rectangle
3. Triangle
4. Circle
5. Exit   

Which shape do you want? """)
#Calculating
if shape == "5":
    print("Exiting the program. Goodbye!")
    exit()
elif shape == "1": #Square
    base = float(input("Side: "))
    while base <=0:
        print("Please enter a positive number.")
        base = float(input("Side: "))
    print("The area is", base**2)
    used = used+1
elif shape == "2": #Rectangle
    length = float(input("Length: "))
    width = float(input("Width: "))
    while length <= 0 or width <= 0:
        print("Please enter positive numbers.")
        length = float(input("Length: "))
        width = float(input("Width: "))
    print("The area is", length*width)
    used = used+1
elif shape == "3": #Triangle
    base = float(input("Base: "))
    height = float(input("Height: "))
    while base<= 0 or height <= 0:
        print("Please enter positive numbers.")
        base = float(input("Base: "))
        height = float(input("Height: "))
    print("The area is", (base*height)*0.5)
    used = used+1
elif shape == "4": #Circle
    radius = float(input("Radius: "))
    while radius <=0:
        print("Please enter a positive number.")
        radius = float(input("Radius: "))
    print("The area is", math.pi*(radius**2))
    used = used+1
else:
    print("Invalid choice. Please choose a valid choice from 1 to 5.")
if used>0:
    print("Thank you for using the Area Calculator!")
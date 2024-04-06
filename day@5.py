import math

def square_area(side):
    return side * side

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return math.pi * (radius ** 2)

# Ask the user for their choice of shape
shape = input("Enter the shape (square, rectangle, triangle, circle): ").lower()

# Calculate and display the area based on the shape chosen
if shape == "square":
    side = float(input("Enter the length of a side: "))
    print("Area of the square:", square_area(side))
elif shape == "rectangle":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    print("Area of the rectangle:", rectangle_area(length, width))
elif shape == "triangle":
    base = float(input("Enter the base length: "))
    height = float(input("Enter the height: "))
    print("Area of the triangle:", triangle_area(base, height))
elif shape == "circle":
    radius = float(input("Enter the radius: "))
    print("Area of the circle:", circle_area(radius))
else:
    print("Invalid shape entered.")
    klnf

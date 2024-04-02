# Define a function to calculate the area of a circle
def calculate_area(radius):
    pi = 3.14159  # Value of Pi
    area = pi * radius * radius
    return area

# Ask the user to input the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate the area using the function
area = calculate_area(radius)

# Print the result
print("The area of the circle with radius", radius, "is:", area)

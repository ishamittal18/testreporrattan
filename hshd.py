# Function to calculate the area of a rectangle
def calculate_area(length, width):
    return length * width

# Input the length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area
area = calculate_area(length, width)

# Print the result
print(f"The area of the rectangle is: {area}")

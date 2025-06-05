import math


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

 

add_result = add(5, 3)
subtract_result = subtract(10, 4)

multiply_result = multiply(6, 7)
divide_result = divide(20, 5)

# def area_of_rectangle(length, width):
#     return length * width

# def area_of_circle(radius):
#     return math.pi * (radius ** 2)

# def area_of_triangle(base, height):
#     return 0.5 * base * height

# Test the area functions
# rect_area = area_of_rectangle(5, 4)
# circle_area = area_of_circle(3)
# triangle_area = area_of_triangle(6, 8)

# print(f"Rectangle area: {rect_area}")
# print(f"Circle area: {circle_area:.2f}")
# print(f"Triangle area: {triangle_area}")
print(f"Addition: {add_result}")
print(f"Subtraction: {subtract_result}")    
print(f"Multiplication: {multiply_result}")
print(f"Division: {divide_result}")

multiply_result = multiply(6, 7)
divide_result = divide(20, 5)

print(f"Addition: {add_result}")
print(f"Subtraction: {subtract_result}")    
print(f"Multiplication: {multiply_result}")
print(f"Division: {divide_result}")

#syvia will do area of a rectangle
#murunga will do area of a circle
#rashid will do area of a triangle
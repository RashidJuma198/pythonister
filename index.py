
def add(a, b):
    return a + b

# def subtract(a, b):
#     return a - b
# def multiply(a, b):
#     return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b



add_result = add(5, 3)
# subtract_result = subtract(10, 4)
# multiply_result = multiply(6, 7)
divide_result = divide(20, 5)

print(f"Addition: {add_result}")
# print(f"Subtraction: {subtract_result}")    
# print(f"Multiplication: {multiply_result}")
print(f"Division: {divide_result}")

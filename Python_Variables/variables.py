# Python Variables Exercise Questions
# ===================================

# Questions for Sylvia (1-10):
# 1. Create a variable named 'age' and assign your age to it
# 2. Create a string variable containing your full name
# 3. Create three variables in one line containing your favorite colors
# 4. Define a global variable called 'school_name' and use it inside a function
# 5. Create a variable with a float number and convert it to integer
# 6. Assign the same value to multiple variables in one line
# 7. Create a variable named 'is_student' with boolean value
# 8. Output a variable's value inside a print statement with text
# 9. Create a variable name with multiple words using snake_case
# 10. Declare a constant variable (use uppercase convention)

# Questions for Rashid (11-20):
# 11. Create variables for storing personal details (name, age, city)
# 12. Swap values between two variables without using a third variable
# 13. Create a variable name starting with an underscore
# 14. Combine two variables containing strings
# 15. Create a variable containing a list of numbers
# 16. Use global keyword inside a function to modify a global variable
# 17. Create variables using different number types (int, float, complex)
# 18. Create a variable name using camelCase convention
# 19. Output multiple variables in a single print statement
# 20. Create a variable containing multi-line string

# Questions for Dan (21-30):
# 21. Create variables to store rectangle dimensions and calculate area
# 22. Create a variable name with numbers (not at the beginning)
# 23. Demonstrate variable reassignment
# 24. Create variables for a basic math calculation
# 25. Use type conversion between different variable types
# 26. Create a variable containing a dictionary of personal info
# 27. Define multiple global variables in one line
# 28. Create variables to store and manipulate date information
# 29. Create a variable containing None value
# 30. Create variables for storing currency values with decimals

# Each person can implement their solutions below these comments
# ============================================================

# Sylvia's Implementation Area:


# Rashid's Implementation Area:


# Dan's Implementation Area:
# 21. Create variables to store rectangle dimensions and calculate area
width = eval(input("Enter the width: "))
length = eval(input("Enter the length: "))
rectangle_area = width * length
print("Rectangle Area:", rectangle_area)

# 22. Create a variable name with numbers (not at the beginning)
product1 = "Car"
product_1 = "Bike"

# 23. Demonstrate variable reassignment
height = 25
height = 30
print("Height:", height)

# 24. Create variables for a basic math calculation
first_number = 21
second_number = 51
sum_result = first_number + second_number
print("Sum:", sum_result)

# 25. Use type conversion between different variable types
base_float = 10.5
base_int = int(base_float)
print("Integer:", base_int)

# 26. Create a variable containing a dictionary of personal info
personal_info = {
    "name": "Murunga",
    "age": 23,
    "city": "Kakamega"
}

# 27. Define multiple global variables in one line
university, course, year = "Maseno University", "Mathematics and Economics", 4

# 28. Create variables to store and manipulate date information
from datetime import date
date_year = date.today().year 
date_month = date.today().month
date_day = date.today().day

# 29. Create a variable containing None value
number = None
# 30. Create variables for storing currency values with decimals
price = 19.99
tax = 0.05
total = price + (price * tax)
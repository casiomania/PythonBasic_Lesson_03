# Lesson 03 / Homework 02
# The user enters two numbers.
# Determine whether these numbers are equal, and if not, display them in ascending order

try:
    first_number = int(input("Enter first number (integer): "))
    second_number = int(input("Enter second number (integer): "))

    greater_number = first_number
    if second_number > greater_number:
        greater_number = second_number
    smaller_number = first_number
    if second_number < smaller_number:
        smaller_number = second_number

    if first_number == second_number:
        print("The numbers are equal.")
    else:
        print(f"Numbers in ascending order: {greater_number}, {smaller_number}")

except ValueError as error:
    print(f"Value Error: {error}")
except Exception as error:
    print(f"Exception: {error}")
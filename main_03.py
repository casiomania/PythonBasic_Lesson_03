# Lesson 03 / Homework 03
# The user enters two numbers and a math action: + - * or /.
# Depending on the entered math action, print the result.

try:
    first_number = int(input("Enter first number (integer): "))
    second_number = int(input("Enter second number (integer): "))

    print("1. (+)\n2. (-)\n3. (*)\n4. (/)")

    selection = int(input("Choose math action from menu (1-4): "))

    match selection:
        case 1:
            add = first_number + second_number
            print(f"{first_number} + {second_number} = {add}")
        case 2:
            sub = first_number - second_number
            print(f"{first_number} - {second_number} = {sub}")
        case 3:
            div = first_number * second_number
            print(f"{first_number} * {second_number} = {div}")
        case 4:
            mult = first_number / second_number
            print(f"{first_number} / {second_number} = {mult}")
        case _:
            print("Incorrect menu item!")

except ValueError as error:
    print(f"Value Error: {error}")
except ZeroDivisionError as error:
    print(f"Zero Division Error: {error}")
except Exception as error:
    print(f"Exception: {error}")

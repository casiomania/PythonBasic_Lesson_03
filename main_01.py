# Lesson 03 / Homework 01
# The user enters the day of the week number (1-7) from the keyboard. The name of the day of
# the week should be displayed. For example, if 1, the screen displays Monday, 2 - Tuesday, and so on.

try:
    day = int(input("Enter day of the week (1-7): "))

    match day:
        case 1:
            print("Monday")
        case 2:
            print("Thursday")
        case 3:
            print("Wednesday")
        case 4:
            print("Tuesday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Please enter correct day of the week (1-7).")

except ValueError as error:
    print(f"Value Error: {error}")
except Exception as error:
    print(f"Error: {error}")
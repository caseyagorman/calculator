"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *




def calculator_menu():
    print("Welcome to the calcutor!")
    print("You have the following options: add (a), minus (m), times (t), divide (d), square (s), cube (c), power (p), and remainder (r).")
    print("To see this menu again, type 'options (o)'.")


def calculator_input():
    while True:
        print("You're in the calculator_input function.")
        user_input = raw_input("> ")
        user_input = user_input.split(" ")
        user_choice = user_input[0][0].lower()

        if len(user_input) == 3:
            num1 = int(user_input[1])
            num2 = int(user_input[2])
            print(num1, num2)
            return user_choice, num1, num2
            break

        elif len(user_input) == 2:
            num1 = num1 = int(user_input[1])
            print(num1)
            return user_choice, num1
            break


        elif len(user_input) == 1:
            print ("Please enter a valid command")





def calculator_operations(user_choice, num1, num2):
        print (num1, num2)
        while True:
            print("You're in the calculator_operations function.")
            if user_choice == "a":
                # num1, num2= calculator_input()
                print(add(num1, num2))

            elif user_choice == "m":
                print(minus(num1, num2))

            elif user_choice =="t":
                print(times(num1, num2))

            elif user_choice =="d":
                print(divide(num1, num2))

            elif user_choice =="s":
                print(square(num1))

            elif user_choice == "c":
                print(cube(num1))

            elif user_choice == "p":
                print(divide(num1, num2))

            elif user_choice == "r":
                print(divide(num1, num2))

            else:
                print("This is not an option, please try again")

            calculator_input()


def run_calculator():
        calculator_menu()
        user_choice, num1, num2 = calculator_input()
        calculator_operations(user_choice, num1, num2)


run_calculator()

"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *




def calculator_menu():
    print("Welcome to the calculator!")
    print("You have the following options: add (a), minus (m), times (t), divide (d), square (s), cube (c), power (p), and remainder (r).")
    print("To see this menu again, type 'options (o)'.")


def calculator_input():
    while True:
        user_input = raw_input("> ")
        user_input = user_input.split(" ")
        user_choice = user_input[0][0].lower()
        try:
            nums = list(map(int, user_input[1:]))
            return user_choice, nums
        except ValueError:
            print("Enter one or two numbers")

        if len(user_input) == 1:
            print ("Please enter a valid command")


def calculator_operations(user_choice, nums):
        print (nums)
        while True:
            if len(nums) == 2:
                num1 = nums[0]
                num2 = nums[1]
                print (num1, num2)

                if user_choice == "a":
                    print(add(num1, num2))

                elif user_choice == "m":
                    print(minus(num1, num2))

                elif user_choice =="t":
                    print(times(num1, num2))

                elif user_choice =="d":
                    print(divide(num1, num2))

            elif len(nums) == 1:
                num1 = nums[0]

                if user_choice =="s":
                    print(square(num1))

                elif user_choice == "c":
                      if len(nums) == 1:
                        print(cube(num1))

            else:
                print("This is not an option, please try again")

            user_choice, nums = calculator_input()


def run_calculator():
        calculator_menu()
        user_choice, nums= calculator_input()
        calculator_operations(user_choice, nums)

run_calculator()

"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *




def calculator_menu():
    print("Welcome to the calcutor!")
    print("You have the following options: add (a), subtract (s), times (t), divide (d), square (s), cube (c), power (p), and mod (m).")
    print("To see this menu again, type 'optins (o)'.")

def calculator_input():
    while True:
        user_input = input("> ")
        user_input = user_input.split(" ")

        try:
            try:
                user_input[2]
            except IndexError:
                user_input.append(1)
            num1 = int(user_input[1])
            num2 = int(user_input[2])
            print(num1, num2)
            return num1, num2
            break
        except ValueError:
            print ("enter a number")
            print("FAILED")



#calculator_menu()
#ser_option_choice = user_input[0][0].lower()


calculator_input()
 # if user_option_choice == "a":
 #        add()

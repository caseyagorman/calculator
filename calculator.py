"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculator_menu():
    print("Welcome to the calcutor!")
    print("You have the following options: add (a), subtract (s), times (t), divide (d), square (s), cube (c), power (p), and mod (m).")
    print("To see this menu again, type 'optins (o)'.")

def calculator():
    user_input = input("> ")
    user_input = user_input.split(" ")
   # if user_input[0] ==


calculator_menu()
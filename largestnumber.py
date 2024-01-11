import tkinter as tk
from tkinter import messagebox

#Ask input from the user
def finding_the_largest_number():
    try: 
        #Enter the first number
        num1 = int(input("Enter first number: "))

        #Enter the second number
        num2 = int(input("Enter second number: "))

        #Enter the third number
        num3 = int(input("Enter third number: "))

    # Create a list of the numbers
        numbers = [num1, num2, num3]

    #Compare the 3 given numbers
        if num1 >= num2 and num1 >= num3:
          largest = num1
        elif num2 >= num1 and num2 >= num3:
          largest = num2
        else:
           largest = num3

    #Display the largest number
        result_label.config(text="The largest number is:".format(largest))

    # Sort the numbers in descending order
        numbers.sort(reverse=True)

    # Display the numbers from highest to lowest
        sorted_numbers_print.config(text="Numbers from highest to lowest:".format(numbers))

    except ValueError: 
     messagebox.showerror(title="Error", message="Please enter a valid number.")
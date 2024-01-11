import tkinter as tk
from tkinter import messagebox

#Ask input from the user
def finding_the_largest_number():
    try: 
        #Enter the first number
        num1 = int(firstnumber.get())

        #Enter the second number
        num2 = int(secondnumber.get())

        #Enter the third number
        num3 = int(thirdnumber.get())

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
        sorted_numbers_print.config(text="Numbers from highest to lowest:".format)

    except ValueError: 
        messagebox.showerror(title="Error", message="Please enter a valid number.")

root = tk.Tk()
root.title("Finding the largest digit")

firstnumber = tk.Entry(root, width=20)
secondnumber = tk.Entry(root, width=20)
thirdnumber = tk.Entry(root, width=20)

#Labels
label1 = tk.Label(root, text="Enter first number:")
label2 = tk.Label(root, text="Enter second number:")
label3 = tk.Label(root, text="Enter third number:")
result_label = tk.Label(root, text="")
sorted_numbers_print = tk.Label(root, text="")
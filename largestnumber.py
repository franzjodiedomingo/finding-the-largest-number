import tkinter as tk
from tkinter import messagebox

#Ask input from the user
def find_largest():
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
        result_label.config(text="The largest number is: {}".format(largest))

        # Sort the numbers in descending order
        numbers.sort(reverse=True)

        # Display the numbers from highest to lowest
        sorted_numbers_print.config(text="Numbers from highest to lowest: {}".format(numbers))

    except ValueError: 
        messagebox.showerror(title="Error", message="Please enter a valid number.")

root = tk.Tk()
root.title("Finding the largest digit")

#User input
firstnumber = tk.Entry(root, width=15)
secondnumber = tk.Entry(root, width=15)
thirdnumber = tk.Entry(root, width=15)

#Labels
label1 = tk.Label(root, text="Enter the first number:", font=("Helvetica", 10, "bold"))
label2 = tk.Label(root, text="Enter the second number:", font=("Helvetica", 10, "bold"))
label3 = tk.Label(root, text="Enter the third number:", font=("Helvetica", 10, "bold"))
result_label = tk.Label(root, text="", font=("Helvetica", 10, "bold"))
sorted_numbers_print = tk.Label(root, text="", font=("Helvetica", 10))

#Creating a button
compare_button = tk.Button(root, text="Compare Numbers", command=find_largest, bg='#4caf50', fg='white')


#Layout
label1.grid(row=0, column=0, sticky='w')
firstnumber.grid(row=0, column=1)
label2.grid(row=1, column=0, sticky='w')
secondnumber.grid(row=1, column=1)
label3.grid(row=2, column=0, sticky='w')
thirdnumber.grid(row=2, column=1)

compare_button.grid(row=3, column=0, columnspan=2, pady=10)
result_label.grid(row=4, column=0, columnspan=2)
sorted_numbers_print.grid(row=5, column=0, columnspan=2)

root.mainloop()
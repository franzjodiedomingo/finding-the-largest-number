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

#Window size and position
window_width = 400
window_height = 350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack()
canvas.create_rectangle(0, 0, window_width, window_height, fill="#c7ecee")

#User input
firstnumber = tk.Entry(root, width=30)
secondnumber = tk.Entry(root, width=30)
thirdnumber = tk.Entry(root, width=30)

#Labels
label1 = tk.Label(root, text="Enter the first number:", font=("Helvetica", 10, "bold"), bg="#c7ecee")
label2 = tk.Label(root, text="Enter the second number:", font=("Helvetica", 10, "bold"), bg="#c7ecee")
label3 = tk.Label(root, text="Enter the third number:", font=("Helvetica", 10, "bold"), bg="#c7ecee")
result_label = tk.Label(root, text="", font=("Helvetica", 10, "bold"))
sorted_numbers_print = tk.Label(root, text="", font=("Helvetica", 10, "bold"))

#Creating a button
compare_button = tk.Button(root, text="Compare Numbers", command=find_largest, bg='#4caf50', fg='white')

#Layout
label1.place(x=20, y=35)
firstnumber.place(x=200, y=35)

label2.place(x=20, y=85)
secondnumber.place(x=200, y=85)

label3.place(x=20, y=135)
thirdnumber.place(x=200, y=135)

compare_button.place(x=20, y=185, width=360, height=30)
result_label.place(x=20, y=235, width=360, height=30)
sorted_numbers_print.place(x=20, y=285, width=360, height=30)

root.mainloop()
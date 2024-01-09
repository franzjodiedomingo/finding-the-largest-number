#Ask input from the user

#Enter the first number
num1 = (input("Enter first number: "))

#Enter the second number
num2 = (input("Enter second number: "))

#Enter the third number
num3 = (input("Enter third number: "))

#Compare the 3 given numbers
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

#Print the largest number
print("The largest number is: ", largest)

# Create a list of the numbers
numbers = [num1, num2, num3]

# Sort the numbers in descending order
numbers.sort(reverse=True)

# Display the numbers from highest to lowest
print("Numbers from highest to lowest:")
for number in numbers:
    print(number)
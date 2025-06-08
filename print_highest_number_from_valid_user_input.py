numbers = []

#ask for user input
num = float(input("Enter a number: "))
numbers.append(num)

#print highest number
if numbers:
    print("The highest number is ", max(numbers))
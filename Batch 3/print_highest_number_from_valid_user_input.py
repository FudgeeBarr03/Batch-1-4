numbers = []

while True:
    try:
        #ask for user input
        num = float(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

#print highest number
if numbers:
    print("The highest number is ", max(numbers))
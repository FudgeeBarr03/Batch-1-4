numbers = []

#create while loop and check if user input is valid
while True:
    try:
        #ask for user input
        num = float(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

#get the average of the numbers by dividing the sum of all the number by the total amount of numbers
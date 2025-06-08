#create an initial library for numbers
numbers = []

#create a loop asking for user input
while True:
    try:
        num = int(input("Enter a number:"))
        numbers.append(num)
    #add a checker if number is a duplicate or if its unique
        if numbers.count(num) > 1:
            print("Duplicate")
        else:
            print("Unique")
#if user enters an invalid input, break
    except ValueError:
        print("Input is invalid. Terminating program.")
        break
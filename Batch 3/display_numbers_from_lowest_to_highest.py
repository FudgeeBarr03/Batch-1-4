numbers = []

#create loop to check if user input is valid
while True:
    try:
        #ask for user input
        num = float(input("Enter a number: "))
        #add numbers to list
        numbers.append(num)
    except ValueError:
        break

#sort numbers
if numbers:
    numbers.sort()
    print("The numbers in ascending order:")
    #print sorted numbers
    for n in numbers:
        print(n)

numbers = []

#ask for user input
num = float(input("Enter a number: "))
#add numbers to list
numbers.append(num)

#sort numbers
if numbers:
    numbers.sort
    print("The numbers in ascending order:")
    #print sorted numbers
    for n in numbers:
        print(n)

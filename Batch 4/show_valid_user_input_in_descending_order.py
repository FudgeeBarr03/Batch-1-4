numbers = []

#create while loop and check for valid input
while True:
    try:
        #ask for user input
        num = float(input("Enter a number: "))
        #store numbers
        numbers.append(num)
    except ValueError:
        break

#use sort() to arrange numbers
if numbers:
    numbers.sort(reverse=True)
    print("Numbers in descending order:")
    #print  the numbers in descending order
    for n in numbers:
        print(n)        
numbers = []

#ask for user input
num = float(input("Enter a number: "))
#store numbers
numbers.append(num)

#use sort() to arrange numbers
if numbers:
    numbers.sort(reverse=True)
    print("Numbers in descending order:")
    #print  the numbers in descending order
    for n in numbers:
        print(n)        
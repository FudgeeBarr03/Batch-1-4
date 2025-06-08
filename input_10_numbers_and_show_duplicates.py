numbers = []

#ask for user input
for i in range(10):
    num = input("Enter a number: ")
    #store user input
    numbers.append(num)

duplicate = []
#check for duplicates
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicate:
        duplicate.append(num)
#print the duplicates
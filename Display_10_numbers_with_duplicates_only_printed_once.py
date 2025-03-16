#ask for user input
numbers = []
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)     #store values

#check for duplicated values and store first instance
first_time_num = []
duplicate_numbers = []
for num in numbers:
    if num not in duplicate_numbers:
        first_time_num.append(num)
        duplicate_numbers.append(num)

#print duplicate values once
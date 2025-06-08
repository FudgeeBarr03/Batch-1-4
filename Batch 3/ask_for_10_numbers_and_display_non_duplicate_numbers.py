#initialize numbers
#ask for input
numbers = []
for i in range(10):
    num = int(input("enter a number: "))
    numbers.append (num) #store numbers

#check for duplicate numbers
unique_numbers = []
for num in numbers:
    if numbers.count(num) == 1:
        unique_numbers.append(num)

#print numbers that do not have a duplicate
print("the unique numbers are: ", unique_numbers)
#Ask for 10 numbers input
numbers = []
for i in range(10):
    num = int(input("enter a number: "))
    numbers.append(num)
    
#subtract first number from all the other numbers
result = numbers[0]
for num in numbers[1:]:
    result -= num

#print difference
print("The first number minus the remaining numbers is ", result)
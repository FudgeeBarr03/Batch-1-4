#initialize odd numbers count
odd_numbers = 0

#input 10 numbers
for i in range(10):
    num = float(input("enter a number: "))
    if num % 2 != 0:
        odd_numbers +=1
        
#output odd numbers
#input 10 numbers
even_numbers = 0

for i in range(10):
    num = int(input("enter a number: "))
    if num % 2 == 0:
        even_numbers += 1

#output how many odd numbers are there
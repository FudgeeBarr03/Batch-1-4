#ask for two numbers
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

#output the smaller one
if num1 < num2:
    print(f"{num1} is smaller than {num2}")
else:
    print(f"{num2} is smaller than {num1}")
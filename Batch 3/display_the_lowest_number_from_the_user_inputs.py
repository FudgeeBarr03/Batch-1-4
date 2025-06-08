numbers = []

#Ask for user's input numbers
while True:
    try:
        num = float(input("Enter a number: "))
        #add numbers into empty list
        numbers.append(num)
    except ValueError:
        break 
    
#print the lowest number
if numbers:
    print("Lowest number entered:", min(numbers))
else:
    print("No valid numbers were entered.")
numbers = []

#Ask for user's input numbers
while True:
    try:
        num = float(input("enter a number"))
        #add numbers into empty list
        numbers.append(num)
    except ValueError:
        break 
    
#print the lowest number
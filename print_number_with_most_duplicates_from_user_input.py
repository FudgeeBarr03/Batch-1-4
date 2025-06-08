numbers = []

#create loop and check for valid user input
while True:
    try:
        #ask for user input until invalid input
        num = float(input("Enter a number: "))
        #store values
        numbers.append(num)
    except ValueError:
        break

#check and print most duplicated number 
if numbers:
    max_count = 1
    most_duplicate = None
    
    for num in numbers:
        count = numbers.count(num)
        if count > max_count:
            max_count = count
            most_repeated = num

    if max_count > 1:
        print(f"Most duplicated number: {most_duplicate} (appeared {max_count} times)")
    else:
        print("No duplicates found.")
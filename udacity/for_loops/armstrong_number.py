num = input("Enter any Number: ")
total = 0
for i in num:
    total += int(i) ** len(num)
    
    new_total = str(total)
    if new_total == num:
        print("The ", num, "is an Armstrong number")
    else:
        print("The", num, "is not an Armstrong number")

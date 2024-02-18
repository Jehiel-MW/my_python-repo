num = input("Enter any number(s): ")

even = 0
odd = 0

for number in num:
    if int(number) % 2 == 0:
        even += 1
        print(even)
    elif int(number) % 2 == 1:
        odd += 1
        print(odd)
    else:
        print("I don't think this is an Integer")

def calculator():
    value_1 = float(input("Enter first value: "))
    value_2 = float(input("Enter second value: "))



    # Operation choice

    print("Choose Operation")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (x)")
    print("4. Division (÷)")
    print("5. Modulus (%)")
    print("6. Exponential/Power (^n)")
    print("7. Root (n√)\n")

    # Choice Selection

    choice = input("Enter an Operation Code 1/2/3/4/5/6/7: ")
    
    # Control statement
    if choice == "1":
        add = value_1 + value_2
        print(add)
        print("\n")
    elif choice == "2":
        minus = value_1 - value_2
        print(minus)
        print("\n")
    elif choice == "3":
        multiply = value_1 * value_2
        print(multiply)
        print("\n")
    elif choice == "4":
        divide = value_1 / value_2
        print(divide)
        print("\n")
    elif choice == "5":
        mod = value_1 % value_2
        print(mod)
        print("\n")
    elif choice == "6":
        exp = value_1 ** value_2
        print(exp)
        print("\n")
    elif choice == "7":
        root_numb = 1/value_2
        root = value_1 ** root_numb
        print(root)
        print("\n")
    else:
        print("You made a wrong choice\n\n")

    reuse = input("Do you want to try some other operation(yes/no): ")
    if reuse.lower() == "yes":
        print("\n")
        calculator()
    else:
        print("Thanks for allowing us to help you")


calculator()


def process_inputs():
    list_input = []
    tuple_input = ()

    list_length = 5
    tuple_length = 3

    for i in range(list_length):
        while True:
            try:
                user_input = int(input("Enter a digit: "))
                list_input.append(user_input)
                break
            except ValueError:
                print("Invalid input. Enter a digit")

    for i in range(tuple_length):
        while True:
            try:
                user_input = input("Enter a value: ")
                my_list = list(tuple_input)
                my_list.append(user_input)
                break
            except ValueError:
                print("Invalid input. Enter a string")
        tuple_input = tuple(my_list)

    new_list = list(tuple_input)
    tuple_input = tuple(list_input)
    list_input = new_list
    print(list_input)
    print(tuple_input)

    new_list = list(tuple_input)
    new_list.sort()
    print(new_list)

    print(list_input)
    new_tuple = tuple(new_list) + tuple(list_input)
    print(new_tuple)

# Call the function to run the program
process_inputs()

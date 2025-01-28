def process_input_list():
    list_input = []

    # Get the length of the list from the user
    while True:
        try:
            list_length = int(input("Enter the list length: "))
            break
        except ValueError:
            print("Invalid input. Enter a digit.")

    # Collect values for the list
    for length in range(list_length):
        while True:
            user_input = input("Enter list value: ")
            try:
                # Attempt to convert input to an integer
                user_input_int = int(user_input)
                list_input.append(user_input_int)
                break
            except ValueError:
                # If conversion fails, treat input as a string
                list_input.append(user_input)
                break

    # Calculate the sum of integers and reverse the strings
    sum = 0
    for i in range(len(list_input)):
        if isinstance(list_input[i], int):  # Check if the item is an integer
            sum += list_input[i]
        elif isinstance(list_input[i], str):  # Check if the item is a string
            list_input[i] = list_input[i][::-1]  # Reverse the string in the list

    # Print the results
    print("Reversed list:", list_input)
    print("Sum of integers:", sum)

# Call the function to test
process_input_list()
